using UnityEngine;
// using UnityEngine.Tilemaps;

public class Teleport : MonoBehaviour 
{
    public Transform player; // Assign the Player Tilemap in the Inspector

    private void Start()
{
    
    GameObject playerObject = GameObject.FindWithTag("Player"); 
        {
            player = playerObject.transform;
            Debug.Log("Spieler erfolgreich gefunden!");
        }
        
    }


    private void OnTriggerEnter2D(Collider2D other)
        {
            if (other.gameObject.CompareTag("Exit")) // Check if Player enters
            {
                player.position = new Vector3(player.transform.position.x, -47f, player.transform.position.z); // Player teleportieren
            }
        }
}   