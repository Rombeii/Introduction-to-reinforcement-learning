using UnityEngine;

public class MovingPlane : MonoBehaviour
{
    private Vector3 startingPos;
    private Rigidbody rb;
    [SerializeField] private Vector3 direction;
    [SerializeField] private float maxDistance;
    [SerializeField] private float velocityMultiplier;
    
    private void Start()
    {
        startingPos = transform.localPosition;
        rb = GetComponent<Rigidbody>();
    }

    void Update()
    {
        float dist = Vector3.Distance(startingPos, transform.localPosition);
        if (dist < maxDistance)
        {
            rb.AddForce(direction * velocityMultiplier);    
        }
        else
        {
            rb.AddForce((startingPos - transform.localPosition) * velocityMultiplier);
        }
        
    }

    public void resetPosition()
    {
        transform.localPosition = startingPos;
        rb.angularVelocity = Vector3.zero;
        rb.velocity = Vector3.zero;
        transform.rotation = Quaternion.identity;
    }
}
