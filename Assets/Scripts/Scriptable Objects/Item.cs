using System.ComponentModel;
using UnityEngine;

[CreateAssetMenu(fileName ="New Item", menuName ="Item/Create New Item")]

public class Item : ScriptableObject
{
    public int id;              // unique identifier, short and easy to adress but not easy to read
    public string idName;       // unique identifier, longer, not much harder to adress and a bliss to read (in comparison)
    // both have to be appointed manually right now
    public string itemName;     // should be plural for most resources and singular for most tools etc.
    public int value;           // market value/price, for future use
    public Sprite icon;
    public ItemType itemType;
}

public enum ItemType
{
    Default,
    Tools,
    Farming,
    Miscellaneous
}


/*
How to create an item
1. (In Assets/Items) Right Click -> Create -> Item -> Create New Item
2. Name it properly and fill out all input fields and give it a sprite (this one is shown in the inventory)
3. In Resources -> Prefabs: Right Click -> Create -> Scene -> Prefab
4. Add a sprite renderer and a sprite (this is the one shown in the world as a dropped item), 
   RigidBody (Kinematic, simulated), a collider (box or circle), ItemPickup.cs 
   and ItemController.cs (and assign the corresponding item)
4. or duplicate the "Item" prefab and assign everything properly

*/