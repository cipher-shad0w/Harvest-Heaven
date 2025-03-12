// using Unity.VisualScripting; // Removed unnecessary using directive
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
    }

    void AnimateMovement(Vector3 direction)
    {

        animator.SetFloat("Horizontal", direction.x);
        animator.SetFloat("Vertical", direction.y);
        animator.SetFloat("Speed", direction.sqrMagnitude);
    }


}
