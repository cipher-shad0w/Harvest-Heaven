using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class InventoryManager : MonoBehaviour
{
    public static InventoryManager Instance;
    public List<Item> Items = new List<Item>();
    public Transform ItemContent;
    public GameObject InventoryItem;

    public bool isInventoryOpen = false;

    public delegate void InventoryToggled(bool state);
    public event InventoryToggled OnInventoryToggled;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void Start()
    {
        // Load the Inventory scene additively, but keep it inactive
        SceneManager.LoadSceneAsync("Inventory", LoadSceneMode.Additive).completed += (op) =>
        {
            Scene inventoryScene = SceneManager.GetSceneByName("Inventory");
            foreach (GameObject obj in inventoryScene.GetRootGameObjects())
            {
                obj.SetActive(false); // Keep everything inactive until needed
            }
        };
    }

    public void ToggleInventory()
    {
        if (isInventoryOpen)
        {
            CloseInventory();
        }
        else
        {
            OpenInventory();
        }
    }

    public void OpenInventory()
    {
        isInventoryOpen = true;
        Scene inventoryScene = SceneManager.GetSceneByName("Inventory");

        foreach (GameObject obj in inventoryScene.GetRootGameObjects())
        {
            obj.SetActive(true); // Activate objects
        }

        // 🔹 Assign ItemContent AFTER the Inventory scene is active
        if (ItemContent == null)
        {
            ItemContent = GameObject.Find("Canvas/Panel/Inventory (Scroll View)/Viewport/Content")?.transform;
            if (ItemContent == null)
            {
                Debug.LogError("InventoryManager: ItemContent not found! Check UI hierarchy.");
                return;
            }
        }

        // 🔹 Load the InventoryItem prefab dynamically from Resources
        if (InventoryItem == null)
        {
            InventoryItem = Resources.Load<GameObject>("Prefabs/UI/InventoryItem");
            if (InventoryItem == null)
            {
                Debug.LogError("InventoryManager: InventoryItem prefab not found! Make sure it's inside Resources/Prefabs/UI/");
                return;
            }
        }

        ListItems();
        OnInventoryToggled?.Invoke(isInventoryOpen);
    }

    public void CloseInventory()
    {
        isInventoryOpen = false;
        Scene inventoryScene = SceneManager.GetSceneByName("Inventory");

        foreach (GameObject obj in inventoryScene.GetRootGameObjects())
        {
            obj.SetActive(false); // Deactivate objects instead of unloading the scene
        }

        OnInventoryToggled?.Invoke(isInventoryOpen);
    }

    public void Add(Item item)
    {
        Items.Add(item);
    }

    public void Remove(Item item)
    {
        Items.Remove(item);
    }

    public void ListItems()
    {
        // 🔹 Prevent running if ItemContent or InventoryItem is missing
        if (ItemContent == null)
        {
            Debug.LogError("InventoryManager: ItemContent is null. Make sure the Inventory UI is loaded.");
            return;
        }

        if (InventoryItem == null)
        {
            Debug.LogError("InventoryManager: InventoryItem is null. Ensure the prefab is loaded.");
            return;
        }

        // 🔹 Clear previous items before adding new ones
        foreach (Transform child in ItemContent)
        {
            Destroy(child.gameObject);
        }

        // 🔹 Populate inventory UI with items
        foreach (var item in Items)
        {
            GameObject obj = Instantiate(InventoryItem, ItemContent);
            var itemName = obj.transform.Find("ItemName (Text (TMP))").GetComponent<Text>();
            var itemIcon = obj.transform.Find("Image").GetComponent<Image>();

            itemName.text = item.itemName;
            itemIcon.sprite = item.icon;
        }
    }
}
