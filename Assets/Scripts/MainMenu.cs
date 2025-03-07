using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    public void Play_Game()
    {
        SceneManager.LoadSceneAsync(1);
        SceneManager.LoadSceneAsync("UI", LoadSceneMode.Additive);
    }
    public void Options()
    {
        SceneManager.LoadSceneAsync("Options");
    }
    public void Quit_Game()
    {
        Application.Quit();
    }
}
