using UnityEngine;

public class FarmTile : MonoBehaviour
{
    public bool isPlanted = false;
    public GameObject seedPrefab;

    public void PlantSeed()
    {
        if (!isPlanted)
        {
            Vector3 spawnPosition = GetComponent<Collider2D>().bounds.center;
            spawnPosition.z = 0;

            GameObject seed = Instantiate(seedPrefab, spawnPosition, Quaternion.identity);
            seed.transform.SetParent(transform, false);

            isPlanted = true;
        }
    }
}
