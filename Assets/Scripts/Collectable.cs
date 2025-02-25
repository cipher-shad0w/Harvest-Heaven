using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Collectable : MonoBehaviour
{

    public CollectableType type;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        PlayerController player = collision.GetComponent<PlayerController>();

        if (player)
        {
            player.inventory.Add(type);
            Destroy(this.gameObject);
        }
    }
}

public enum CollectableType
{
    NONE, APPLE, ORANGE, PEAR, CHERRY, STRAWBERRY, GRAPES, BLUEBERRY 
}
