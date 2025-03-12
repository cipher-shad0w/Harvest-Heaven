using System.Collections;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float moveSpeed;
    public Rigidbody2D rb;
    public Animator animator;

    public Inventory inventory;

    private void Awake()
    {
        inventory = new Inventory(21);
    }

    void AnimateMovement(Vector3 direction)
    {

        animator.SetFloat("Horizontal", direction.x);
        animator.SetFloat("Vertical", direction.y);
        animator.SetFloat("Speed", direction.sqrMagnitude);
    }

    private void TryPlantSeed()
    {
        RaycastHit2D hit = Physics2D.BoxCast(transform.position, Vector2.one * 0.2f, 0, Vector2.zero);

        if (hit.collider != null)
        {
            FarmTile farmTile = hit.collider.GetComponent<FarmTile>();

            if (farmTile != null)
            {
                farmTile.PlantSeed();
            }
        }
    }

    private void Update()
    {
        float horizontal = Input.GetAxisRaw("Horizontal");
        float vertical = Input.GetAxisRaw("Vertical");

        Vector3 direction = new Vector3(horizontal, vertical).normalized;

        AnimateMovement(direction);

        transform.position += direction * moveSpeed * Time.deltaTime;
        
        if (Input.GetKeyDown(KeyCode.I))
        {
            InventoryManager.Instance.ToggleInventory();
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            TryPlantSeed();
        }
    }
}
