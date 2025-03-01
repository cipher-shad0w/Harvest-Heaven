using UnityEngine;
using UnityEngine.UI;

public class CloseInventoryButton : MonoBehaviour
{
    private void Start()
    {
        GetComponent<Button>().onClick.AddListener(CloseInventory);
    }

    public void CloseInventory()
    {
        InventoryManager.Instance.CloseInventory();
    }
}
