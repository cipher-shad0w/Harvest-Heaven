public class FarmTile : MonoBehaviour
{
    public bool isPlanted = false;
    public GameObject plantPrefab; // Prefab mit "Plant.cs"

    public void PlantSeed()
    {
        if (!isPlanted)
        {
            Vector3 spawnPosition = GetComponent<Collider2D>().bounds.center;
            spawnPosition.z = 0; 

            Instantiate(plantPrefab, spawnPosition, Quaternion.identity);
            isPlanted = true;
        }
    }
}
