import aicrowd_gym 
import numpy as np
import matplotlib.pyplot as plt
counter = 0

def softmax(x):
    fx = np.exp(x - np.amax(x)) / np.sum(np.exp(x - np.amax(x)))
    return fx




def PolGrad(env,Episodes,trajectory_sample,max_traj_length, alpha):
    
   
    state_dim    = np.prod(env.observation_space.shape) # state dimensionality
    action_dim   = env.action_space.n                   # action dimensionality
    print(state_dim,action_dim)
    ################################
    ##### Declaring Soft weight ####
    ################################
    weights = np.random.normal(0, 1 / np.sqrt(state_dim),(action_dim, state_dim))
    
    ################################
    ######### Storage  #############
    ################################
    rewards           = [0] * Episodes
    
    ################################
    ########## Training ############
    ################################
    for epi in range(Episodes):
        trajectory_reward = 0 
        grad              = np.zeros_like(weights)
        
        for tau in range(trajectory_sample):
            state = env.reset()
            ##### sampling the trajectory ######
            for t in range(max_traj_length):
                prob_actions           = softmax(np.matmul(weights, state.reshape(state_dim, 1)))
                action_choice          = np.random.choice(action_dim, p=prob_actions.flatten())
                
                state, reward, done, _ = env.step(action_choice)
        
                if done:
                    break
                  
                trajectory_reward += 0.95*reward
        
                ######### applying one hot  ####### 
                prob_actions = -prob_actions
                prob_actions[action_choice] += 1
                ######### Gradient Calculation #####
                grad += np.matmul( (prob_actions * reward).reshape(action_dim, 1),state.reshape(1, state_dim))
        
                # Apply gradient (see derivations for subtraction) 
                weights -= alpha * grad / trajectory_sample
        
                rewards[epi] = trajectory_reward / trajectory_sample
    
    return weights,rewards
    
    
def Report(env,weights,rewards,Episodes,trajectory_sample,max_traj_length, alpha):
    plt.figure(figsize=(9,6))
    plt.plot(rewards,color="g",label="alpha = 0.001, gamma = 0.8")
    plt.xlabel("Number of Episodes")
    plt.ylabel("Rewards")
    plt.title("Taxi Agent Training by Q-learning Method")
    plt.legend(loc="best")
    plt.grid()
    plt.show()
    
    ###########################
    ####### Rendering #########
    ###########################
    for i in range(3):
        state = env.reset()
        for j in range(max_traj_length):
            env.render()
            prob_actions           = softmax(np.matmul(weights, state))
            action_choice          = np.random.choice(env.action_space.n, p=prob_actions)
            state, reward, done, _ = env.step(action_choice)
            if done:
                print("Test" + str(i)+" : has done with "+ str(j)+ " steps")
                break
            
    env.close()
        


########################################
############## Execution ###############
########################################
import time 
start = time.time()
env                = aicrowd_gym.make('Acrobot-v1')
Episodes           = 250
alpha              = 0.005
trajectory_sample  = 15
max_traj_length    = 200

weights,rewards    = PolGrad(env,Episodes,trajectory_sample,max_traj_length, alpha)
Report(env,weights,rewards,Episodes,trajectory_sample,max_traj_length, alpha)
end = time.time()
np.save("T300.npy",rewards)
print("Time Taken for the training : " ,(end-start)/60,"minutes")
print("Mean of the reward: ",np.mean(rewards[-500:]))
############################################
############## End #########################
############################################