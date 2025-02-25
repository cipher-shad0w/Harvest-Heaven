using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    [SerializeField] private Transform target;

    Vector3 camOffset;
    void Start()
    {
        camOffset = transform.position - target.position;
    }

    private void FixedUpdate()
    {
        transform.position = target.position + camOffset;
    }
}
