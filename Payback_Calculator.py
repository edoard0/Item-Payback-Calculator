class Payback_Tracker:
  
       
    def __init__(self, name,initial_cost,usage_benefit,frequency,period):
      self.name = name
      self.initial_cost=-float(initial_cost)
      self.usage_benefit=float(usage_benefit)
      self.frequency=int(frequency)
      self.outstanding_balance=float(initial_cost)
      self.period=period
      self.balance_history=[float(initial_cost)]
      self.payback_counter_period=0
      self.usage_total=0
      
    def get_result(self):
      
      import math
      
      if self.period !="day":
        return "At the given {} usage rate, you are expected to payback this {} after {} uses, or {} {}".format(
      self.period+"ly",
      self.name.lower(),
      str(math.ceil(abs(self.initial_cost)/self.usage_benefit)),
      str(math.ceil((abs(self.initial_cost))/(self.frequency*self.usage_benefit))),
      self.period+"s")
      else:
        return "At the given daily usage rate, you are expected to payback this {} after {} uses, or {} {}".format(
      self.name.lower(),
      str(math.ceil(abs(self.initial_cost)/self.usage_benefit)),
      str(math.ceil((abs(self.initial_cost))/(self.frequency*self.usage_benefit))),
      self.period+"s")
        
      
      
    def generate_balance_history(self):
        
      while self.usage_total<=self.outstanding_balance:
        self.single_usage_period=self.usage_benefit*self.frequency
        self.usage_total+=self.single_usage_period
        self.payback_counter_period+=1
        if self.balance_history[-1]<=self.single_usage_period:
          break
        else:
          self.balance_history.append(round(self.outstanding_balance-round(self.payback_counter_period*self.single_usage_period,2))) 
    
         
    def get_balance_history(self):
        return self.balance_history
    
 
    def get_balance_data(self):
      
        import pandas as pd
        
        balance_history_formatted=[self.balance_history[i] for i in range(0,len(self.balance_history))]
        x_axis=[i+1 for i in list(range(len(balance_history_formatted)))]
        
        df=pd.DataFrame({self.period:x_axis,"Balance History":balance_history_formatted})
        
        return df

