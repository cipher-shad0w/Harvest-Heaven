using UnityEngine;
using UnityEngine.SceneManagement;

public class PauseMenu : MonoBehaviour
{
    public GameObject pauseMenu;
    public bool isPaused = false;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
        {
            SceneManager.LoadScene("PauseMenu", LoadSceneMode.Additive);
            StartCoroutine(FindPauseMenu()); // Ensure we find it after the scene loads
        }

        private System.Collections.IEnumerator FindPauseMenu()
        {
            yield return new WaitForSeconds(0.1f); // Give time for the scene to load

            GameObject panel = GameObject.Find("PauseMenu");
            if (panel != null)
            {
                pauseMenu = panel;
                pauseMenu.SetActive(false);
            }
            else
            {
                Debug.LogError("PauseMenu panel not found in loaded scene!");
            }
        }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            if(isPaused)
            {
                ResumeGame();
            }
            else
            {
                PauseGame();
            }
        }
    }

    public void PauseGame()
    {
        // pauseMenu.SetActive(true);
        Time.timeScale = 0f;
        pauseMenu.SetActive(true);
        isPaused = true;
    }

    public void ResumeGame()
    {
        // pauseMenu.SetActive(false);
        Time.timeScale = 1f;
        
        pauseMenu.SetActive(false);
        isPaused = false;
    }

    public void SaveGame()
    {

    }

    public void LoadGame()
    {

    }

    public void Options()
    {
        SceneManager.LoadSceneAsync("Options");
    }

    public void MainMenu()
    {
        isPaused = false;
        SceneManager.LoadSceneAsync("MainMenu");
    }
    public void Quit_Game()
    {
        Application.Quit();
    }
}
