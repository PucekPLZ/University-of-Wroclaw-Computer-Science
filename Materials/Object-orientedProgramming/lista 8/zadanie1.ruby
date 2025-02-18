class Mass
    def initialize(kilogram)
        @kilogram = kilogram
    end
  
    def kilogram
        @kilogram
    end
  
    def pound
        @kilogram * 2.20462
    end
  
    def pound=(pound)
        @kilogram = pound / 2.20462
    end
end
  
class Length
    def initialize(meter)
        @meter = meter
    end
  
    def meter
        @meter
    end
  
    def feet
        @meter * 3.28084
    end
  
    def feet=(feet)
        @meter = feet / 3.28084
    end
end
  
class Area
    def initialize(length, width)
        @length = Length.new(length)
        @width = Length.new(width)
    end
  
    def square_meter
        @length.meter * @width.meter
    end
  
    def hectare
        square_meter * 0.0001
    end
  
    def square_inch
        square_meter / 0.00064516
    end
end
  
class Pressure
    def initialize(mass, area)
        @mass = Mass.new(mass)
        @area = Area.new(area, 1) 
    end
  
    def psi
        @mass.pound / @area.square_inch
    end
    
    def pascal 
        psi * 6894.8
    end

    def bar 
        psi * 0.068948
    end
end
  
puts "Powierzchnia (metr kwadratowy i cal kwadratowy)"

(1..10).each do |x|
    area = Area.new(x, 1)
    puts "#{area.square_meter}     #{area.square_inch}"
end

puts ""

puts "Ciśnienie (paskal i psi)"

(1..10).each do |x|
    pressure = Pressure.new(x, 10)
    puts "#{pressure.pascal}     #{pressure.psi}"
end

