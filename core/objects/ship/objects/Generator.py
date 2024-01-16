


from core.objects.ship.objects.machine import Machine

from core.general.error.error_messages import ALL_PARAMETER_MUST_BE_GREATER_THAN_0


class Generator(Machine):
    
    def __init__(
        self,
        gain= 1,
        efficiency_loss= 0.01,
        heat_gain= 0.01,
        heat_loss= 0.2,
        repair_gain= 0.2,
        max_usage= 1.02,
        voltage = 1.2
    ) -> None:
        
        if (voltage <= 0):
            raise ValueError(ALL_PARAMETER_MUST_BE_GREATER_THAN_0)
        
        super().__init__(gain, efficiency_loss, heat_gain, heat_loss, repair_gain, max_usage)
        
        self.voltage = voltage
        
    def gain_function(self) -> float:
        return self.gain * self.voltage

