using UnityEngine;
using UnityEngine.UI;

public class CloseInventoryButton : MonoBehaviour
{
    private Button closeButton;

    private void Start()
    {
        closeButton = GetComponent<Button>();
        closeButton.onClick.AddListener(CloseInventory);
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            CloseInventory();
        }
    }

    private void CloseInventory()
    {
        InventoryManager.Instance.CloseInventory();
    }
}
