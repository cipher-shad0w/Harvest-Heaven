using UnityEngine;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance;
    // public bool isPaused = false;

    void Awake()
    {
        Instance = this;
    }

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        // if (Input.GetKeyDown(KeyCode.Escape))
        // {
        // PauseMenu
        // }
    }
}