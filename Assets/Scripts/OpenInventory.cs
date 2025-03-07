using UnityEngine;
using UnityEngine.SceneManagement;

public class InventoryManager : MonoBehaviour
{
    public static InventoryManager Instance;
    public bool isInventoryOpen = false;
    private string inventorySceneName = "Inventory";

    public delegate void InventoryToggled(bool state);
    public event InventoryToggled OnInventoryToggled;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject); // Keeps this object across scenes
        }
        else
        {
            Destroy(gameObject);
        }
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
        if (!isInventoryOpen)
        {
            isInventoryOpen = true;
            SceneManager.LoadScene(inventorySceneName, LoadSceneMode.Additive); // Load inventory scene
            OnInventoryToggled?.Invoke(isInventoryOpen);
        }
    }

    public void CloseInventory()
    {
        if (isInventoryOpen)
        {
            isInventoryOpen = false;
            SceneManager.UnloadSceneAsync(inventorySceneName); // Unload inventory scene
            OnInventoryToggled?.Invoke(isInventoryOpen);
        }
    }
}
