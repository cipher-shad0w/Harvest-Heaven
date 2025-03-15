using UnityEngine;

public class NPCDialog : MonoBehaviour
{
    [TextArea]
    public string explanation = 
        "Willkommen in Harvest Heaven!\n" +
        "Ziel.\n" +
        "Steuerung: WASD zum Laufen, Leertaste zum Sammeln un Pflanzen.\n" +
        "Vermeide die dunklen Wölfe im Wald!";

    private bool isPlayerInRange = false;

    private void OnTriggerEnter(Collider other)
    {
        isPlayerInRange = true;
        Debug.Log("Drücke T, um die Spielanleitung zu sehen!");
    }

    private void OnTriggerExit(Collider other)
    {
        
        isPlayerInRange = false;
    }

    private void Update()
    {
        if (isPlayerInRange && Input.GetKeyDown(KeyCode.T))
        {
            Debug.Log(explanation);
        }
    }
}