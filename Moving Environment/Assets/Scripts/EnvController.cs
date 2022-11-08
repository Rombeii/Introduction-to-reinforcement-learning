using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using Unity.MLAgents;

public class EnvController : MonoBehaviour
{
    [SerializeField] private RunnerAgent agent;
    private List<MovingPlane> planes;
    void Start()
    {
        planes = GetComponentsInChildren<MovingPlane>().ToList();
    }

    void Update()
    {
        if (agent.transform.localPosition.y < -1)
        {
            foreach (var plane in planes)
            {
                plane.resetPosition();
            }
            agent.EndEpisode();
        }

        if (agent.TouchedGoal)
        {
            agent.AddReward(100f);
            agent.EndEpisode();
        }
    }
}
