using UnityEngine;

public class FarmTile : MonoBehaviour
{
    public bool isPlanted = false;
    public GameObject seedPrefab;

    public void PlantSeed()
    {
        if (!isPlanted)
        {
            Instantiate(seedPrefab, transform.position, Quaternion.identity);
            isPlanted = true;
        }
    }
}
