using UnityEngine;
using UnityEngine.UI;

public class ButtonHandler : MonoBehaviour
{
    public Button myButton; // Assign this in the Inspector

    void Start()
    {
        if (myButton == null)
            myButton = GetComponent<Button>();

        if (myButton != null)
            myButton.onClick.AddListener(OnButtonClick);
    }

    void OnButtonClick()
    {
        if (PauseMenu.Instance != null)
        {
            PauseMenu.Instance.ResumeGame();
        }
        else
        {
            Debug.LogWarning("GameManager is not found!");
        }
    }
}
