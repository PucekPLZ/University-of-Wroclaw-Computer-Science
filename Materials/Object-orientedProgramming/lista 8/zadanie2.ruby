class Length
    def initialize(meter)
        @meter = meter
    end
  
    def meter
        @meter
    end
  
    def sea_mile
        @meter * 0.000539957
    end
  
    def sea_mile=(sea_mile)
        @meter = sea_mile / 0.000539957
    end
end

class Time
    def initialize(second)
        @second = second
    end
  
    def second
        @second
    end
  
    def hour
        @second / 3600.0
    end
  
    def hour=(hour)
        @second = hour * 3600
    end
end

class Speed
    def initialize(length, time)
        @length = Length.new(length)
        @time = Time.new(time)
    end
  
    def km_per_hour
        (@length.meter / 1000) / @time.hour
    end
  
    def knots
        @length.sea_mile / @time.hour
    end
end
  
class Acceleration
    def initialize(length, time)
        @length = Length.new(length)
        @time = Time.new(time)
    end
    
    def m_per_s2
        @length.meter / @time.second * @time.second
    end

    def km_per_s2
        @length.meter * 0.001 / @time.second * @time.second
    end

    def mm_per_h2
        @length.meter * 1000 / @time.hour * @time.hour
    end
end


puts "Prędkość (kilometry na godzinę i węzły)"

(1000..10000).step(1000).each do |x|
    speed = Speed.new(x, 3600)
    puts "#{speed.km_per_hour}     #{speed.knots}"
end

puts ""

puts "Przyspieszenie (km/s2 i mm/h2)"

(1..10).each do |x|
   acceleration =Acceleration.new(x, 1)
    puts "#{acceleration.m_per_s2}     #{acceleration.km_per_s2}     #{acceleration.mm_per_h2}"
end
