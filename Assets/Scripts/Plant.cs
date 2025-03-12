using UnityEngine;
using System.Collections;

public class Plant : MonoBehaviour
{
    public Sprite[] growthStages;
    private SpriteRenderer spriteRenderer;

    public float growthTime = 5f;
    private int currentStage = 0;

    private void Start()
    {
        spriteRenderer = GetComponent<SpriteRenderer>();
        spriteRenderer.sprite = growthStages[currentStage];

        StartCoroutine(Grow());
    }

    private IEnumerator Grow()
    {
        while (currentStage < growthStages.Length - 1)
        {
            yield return new WaitForSeconds(growthTime);
            currentStage++;
            spriteRenderer.sprite = growthStages[currentStage];
        }
    }
}
