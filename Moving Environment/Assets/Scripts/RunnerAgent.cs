using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Actuators;
using Unity.MLAgents.Sensors;

public class RunnerAgent : Agent
{
    [SerializeField] private float jumpForce = 75f;
    [SerializeField] private float runVelocity = 1f;
    [SerializeField] private int numberOfCheckpoints = 10;
    Rigidbody m_AgentRb;
    private Rigidbody goal_Rb;
    private Dictionary<float, bool> checkpointsReached;
    private float distanceAtStart;
    private bool isGrounded = true;
    private bool touchedGoal = false;

    public override void Initialize()
    {
        m_AgentRb = GetComponent<Rigidbody>();
        goal_Rb = transform.parent.Find("Goal").gameObject.GetComponent<Rigidbody>();
        distanceAtStart = Vector3.Distance(transform.localPosition, goal_Rb.transform.localPosition);
        checkpointsReached = new Dictionary<float, bool>();
        numberOfCheckpoints = 35;
        float inc = distanceAtStart / (numberOfCheckpoints + 1);
        for (int i = 1; i < numberOfCheckpoints; i++)
        {
            checkpointsReached.Add(inc * i, false);
        }
    }
    
    public override void OnActionReceived(ActionBuffers actionBuffers)
    {
        AddReward(-0.001f);
        addRewardBasedOnCheckpoints();
        //AddReward(1f - Vector3.Distance(transform.localPosition, goal_Rb.transform.localPosition) / distanceAtStart);
        MoveAgent(actionBuffers.DiscreteActions);
    }

    private void addRewardBasedOnCheckpoints()
    {
        float distance = Vector3.Distance(transform.localPosition, goal_Rb.transform.localPosition);
        foreach (KeyValuePair<float, bool> entry in checkpointsReached.ToList())
        {
            if (distance < entry.Key && !entry.Value)
            {
                AddReward(1f);
                checkpointsReached[entry.Key] = true;
            }
        }
        
    }

    public void MoveAgent(ActionSegment<int> act)
    {
        var dirToGo = Vector3.zero;
        var rotateDir = Vector3.zero;

        var moveAction = act[0];
        var jumpAction = act[1];

        switch(moveAction)
        {
            case 1:
                dirToGo = transform.forward;
                break;
            case 2:
                rotateDir = transform.up * 0.5f;
                break;
            case 3:
                rotateDir = transform.up * -0.5f;
                break;
        }

        float forceAdded = isGrounded ? runVelocity : runVelocity * 0.6f;
        
        transform.Rotate(rotateDir, Time.deltaTime * 100f);
        m_AgentRb.AddForce(dirToGo * forceAdded, ForceMode.VelocityChange);
        if (jumpAction == 1 && isGrounded)
        {
            m_AgentRb.AddForce(Vector3.up * jumpForce, ForceMode.Force);
        }
    }
    
    void OnTriggerExit(Collider other)
    {
        isGrounded = false;
    }
    
    void OnTriggerEnter(Collider other)
    {
        isGrounded = true;
    }
    
    void OnCollisionEnter(Collision other)
    {
        if (other.gameObject.CompareTag("goalPlane"))
        {
            touchedGoal = true;
        }
    }
    
    public override void CollectObservations(VectorSensor sensor)
    {
        //boolean -> 1 observation
        sensor.AddObservation(isGrounded);
        //rotation of the cube -> 1 observation
        sensor.AddObservation(gameObject.transform.localRotation.eulerAngles.y / 180f);
        //Vector3 -> 3 observations
        sensor.AddObservation(m_AgentRb.velocity.normalized);
        //Vector3 -> 3 observations
        sensor.AddObservation((goal_Rb.transform.localPosition - transform.localPosition).normalized);
    }
    
    public override void Heuristic(in ActionBuffers actionsOut)
    {
        var discreteActionsOut = actionsOut.DiscreteActions;
        if (Input.GetKey(KeyCode.D))
        {
            discreteActionsOut[0] = 2;
        }
        else if (Input.GetKey(KeyCode.W))
        {
            discreteActionsOut[0] = 1;
        }
        else if (Input.GetKey(KeyCode.A))
        {
            discreteActionsOut[0] = 3;
        }
        else if (Input.GetKey(KeyCode.Space))
        {
            discreteActionsOut[1] = 1;
        }
    }
    
    public override void OnEpisodeBegin()
    {
        m_AgentRb.transform.localPosition = new Vector3(0f, 0.5f, 0f);
        m_AgentRb.angularVelocity = Vector3.zero;
        m_AgentRb.velocity = Vector3.zero;
        transform.rotation = Quaternion.identity;
        touchedGoal = false;
        foreach (KeyValuePair<float, bool> entry in checkpointsReached.ToList())
        {
            checkpointsReached[entry.Key] = false;
        }
    }

    public bool TouchedGoal
    {
        get => touchedGoal;
        set => touchedGoal = value;
    }
}
