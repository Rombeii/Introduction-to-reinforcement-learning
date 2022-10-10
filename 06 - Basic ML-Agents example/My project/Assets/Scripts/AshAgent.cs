using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Linq;
using Random = UnityEngine.Random;
using Unity.MLAgents;
using Unity.MLAgents.Actuators;
using Unity.MLAgents.Sensors;

public class AshAgent : Agent
{

    Rigidbody m_AgentRb;
    int ballsCollected = 0;
    public GameObject[] balls;

    public override void Initialize()
    {
        m_AgentRb = GetComponent<Rigidbody>();
    }

    public override void OnActionReceived(ActionBuffers actionBuffers)
    {
        AddReward(-0.001f);
        MoveAgent(actionBuffers.DiscreteActions);
    }

    public void MoveAgent(ActionSegment<int> act)
    {
        var dirToGo = Vector3.zero;
        var rotateDir = Vector3.zero;

        var action = act[0];
        switch (action)
        {
            case 1:
                dirToGo = transform.forward;
                break;
            case 2:
                dirToGo = transform.forward * -1f;
                break;
            case 3:
                rotateDir = transform.up * 0.50f;
                break;
            case 4:
                rotateDir = transform.up * -0.50f;
                break;
        }
        transform.Rotate(rotateDir, Time.deltaTime * 100f);
        m_AgentRb.AddForce(dirToGo * 2f, ForceMode.VelocityChange);
    }

    public override void Heuristic(in ActionBuffers actionsOut)
    {
        var discreteActionsOut = actionsOut.DiscreteActions;
        if (Input.GetKey(KeyCode.D))
        {
            discreteActionsOut[0] = 3;
        }
        else if (Input.GetKey(KeyCode.W))
        {
            discreteActionsOut[0] = 1;
        }
        else if (Input.GetKey(KeyCode.A))
        {
            discreteActionsOut[0] = 4;
        }
        else if (Input.GetKey(KeyCode.S))
        {
            discreteActionsOut[0] = 2;
        }
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("ball"))
        {
            collision.gameObject.SetActive(false);
            AddReward(1f);
            ballsCollected++;
            if(ballsCollected == balls.Length)
            {
                EndEpisode();
            }
        }
    }

    public override void OnEpisodeBegin()
    {
        ballsCollected = 0;
        m_AgentRb.transform.localPosition = new Vector3(0f, 0.5f, 0f);
        foreach (GameObject ball in balls)
        {
            ball.SetActive(true);
            while(true)
            {
                Vector3 spawnPos = new Vector3(Random.Range(-9f, 9f), 1.5f, Random.Range(-9f, 9f));
                if(!Physics.CheckSphere(spawnPos, 1f))
                {
                    ball.transform.localPosition = spawnPos;
                    break;
                }
            }
        }
    }

}
