using UnityEngine;

public class ItemPickup : MonoBehaviour
{
    public Item Item;

    void OnTriggerEnter2D(Collider2D collision)
    {
        Debug.Log("Trigger entered by: " + collision.gameObject.name);

        PlayerController player = collision.GetComponent<PlayerController>();

        if (player)
        {
            Debug.Log("Player detected! Adding item: " + Item.name);
            InventoryManager.Instance.Add(Item);
            Destroy(gameObject);
        }
        else
        {
            Debug.Log("Trigger detected something, but it's not the player.");
        }
    }
}
