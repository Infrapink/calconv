module solar_coords
  implicit none

  ! Calculate ecpliptic coordinates of the sun.
  ! Based on chapter 24 of *Astronomical Algorithms* by Jean Meeus
  ! 2nd Edition, Willman-Bell, 1991
  !
  ! This is the higher-accuracy algorithm
  ! Results can be off by up to 15 minutes, the accuracy apparently varying cyclically.
  ! There doesn't appear to be any more accurate algorithm readily available.

contains
  subroutine solar_tau(jday, tau)
    ! tau will be in Julian millennia
    real(8), intent(in) :: jday ! Julian Day in question
    real(8), intent(out) :: tau

    tau = (jday - 2451545.0) / 365250

  end subroutine solar_tau

  subroutine solar_longitude(jday, longitude)
    ! Ecliptic longitude of Earth
    real(8), intent(in) :: jday
    real(8), intent(out) :: longitude

    ! Value for each term is given by A cos (B + C*tau)
    real(8) :: L
    real(8) :: L0
    real(8) :: L1
    real(8) :: L2
    real(8) :: L3
    real(8) :: L4
    real(8) :: L5

    real(8), dimension(64,3) :: L0terms
    real(8), dimension(34,3) :: L1terms
    real(8), dimension(20,3) :: L2terms
    real(8), dimension(7,3) :: L3terms
    real(8), dimension(3,3) :: L4terms

    real(8) :: tau
    integer :: i
    real(8) :: k
    real(8) :: pi
    real(8) :: pi2

    pi = 4 * atan(1.0)
    pi2 = 2 * pi

    L0terms(1,1) = 175347046.0
    L0terms(1,2) = 0.0
    L0terms(1,3) = 0.0
    L0terms(2,1) = 3341656.0
    L0terms(2,2) = 4.6692568
    L0terms(2,3) = 6283.0758500
    L0terms(3,1) = 34894.0
    L0terms(3,2) = 4.62610
    L0terms(3,3) = 12566.15170
    L0terms(4,1) = 3497.0
    L0terms(4,2) = 2.7441
    L0terms(4,3) = 5753.3849
    L0terms(5,1) = 3418.0
    L0terms(5,2) = 2.8289
    L0terms(5,3) = 3.5231
    L0terms(6,1) = 3136.0
    L0terms(6,2) = 3.6277
    L0terms(6,3) = 77713.7715
    L0terms(7,1) = 2676.0
    L0terms(7,2) = 4.4181
    L0terms(7,3) = 7860.4194
    L0terms(8,1) = 2343.0
    L0terms(8,2) = 6.1352
    L0terms(8,3) = 3930.2097
    L0terms(9,1) = 1324.0
    L0terms(9,2) = 0.7425
    L0terms(9,3) = 11506.7698
    L0terms(10,1) = 1273.0
    L0terms(10,2) = 2.0371
    L0terms(10,3) = 529.6910
    L0terms(11,1) = 1199.0
    L0terms(11,2) = 1.1096
    L0terms(11,3) = 1577.3435
    L0terms(12,1) = 990.0
    L0terms(12,2) = 5.233
    L0terms(12,3) = 5884.927
    L0terms(13,1) = 902.0
    L0terms(13,2) = 2.045
    L0terms(13,3) = 26.298
    L0terms(14,1) = 857.0
    L0terms(14,2) = 3.508
    L0terms(14,3) = 398.149
    L0terms(15,1) = 780.0
    L0terms(15,2) = 1.179
    L0terms(15,3) = 5223.694
    L0terms(16,1) = 753.0
    L0terms(16,2) = 2.533
    L0terms(16,3) = 5507.553
    L0terms(17,1) = 505.0
    L0terms(17,2) = 4.583
    L0terms(17,3) = 18849.228
    L0terms(18,1) = 492.0
    L0terms(18,2) = 4.205
    L0terms(18,3) = 775.523
    L0terms(19,1) = 357.0
    L0terms(19,2) = 2.920
    L0terms(19,3) = 0.067
    L0terms(20,1) = 317.0
    L0terms(20,2) = 5.849
    L0terms(20,3) = 11790.629
    L0terms(21,1) = 284.0
    L0terms(21,2) = 1.899
    L0terms(21,3) = 796.298
    L0terms(22,1) = 271.0
    L0terms(22,2) = 0.315
    L0terms(22,3) = 10977.079
    L0terms(23,1) = 243.0
    L0terms(23,2) = 0.345
    L0terms(23,3) = 5486.778
    L0terms(24,1) = 206.0
    L0terms(24,2) = 4.806
    L0terms(24,3) = 2544.314
    L0terms(25,1) = 205.0
    L0terms(25,2) = 1.869
    L0terms(25,3) = 5573.143
    L0terms(26,1) = 202.0
    L0terms(26,2) = 2.458
    L0terms(26,3) = 6069.777
    L0terms(27,1) = 156.0
    L0terms(27,2) = 0.833
    L0terms(27,3) = 213.299
    L0terms(28,1) = 132.0
    L0terms(28,2) = 3.411
    L0terms(28,3) = 2942.563
    L0terms(29,1) = 126.0
    L0terms(29,2) = 1.083
    L0terms(29,3) = 20.775
    L0terms(30,1) = 115.0
    L0terms(30,2) = 0.645
    L0terms(30,3) = 0.980
    L0terms(31,1) = 103.0
    L0terms(31,2) = 0.636
    L0terms(31,3) = 4694.003
    L0terms(32,1) = 102.0
    L0terms(32,2) = 0.976
    L0terms(32,3) = 15720.839
    L0terms(33,1) = 102.0
    L0terms(33,2) = 4.267
    L0terms(33,3) = 7.114
    L0terms(34,1) = 99.0
    L0terms(34,2) = 6.21
    L0terms(34,3) = 2146.17
    L0terms(35,1) = 98.0
    L0terms(35,2) = 0.58
    L0terms(35,3) = 155.42
    L0terms(36,1) = 86.0
    L0terms(36,2) = 5.98
    L0terms(36,3) = 161000.69
    L0terms(37,1) = 85.0
    L0terms(37,2) = 1.30
    L0terms(37,3) = 6275.96
    L0terms(38,1) = 85.0
    L0terms(38,2) = 3.67
    L0terms(38,3) = 71430.70
    L0terms(39,1) = 80.0
    L0terms(39,2) = 1.81
    L0terms(39,3) = 17260.15
    L0terms(40,1) = 79.0
    L0terms(40,2) = 3.04
    L0terms(40,3) = 12036.46
    L0terms(41,1) = 75.0
    L0terms(41,2) = 1.76
    L0terms(41,3) = 5088.63
    L0terms(42,1) = 74.0
    L0terms(42,2) = 3.50
    L0terms(42,3) = 3154.69
    L0terms(43,1) = 74.0
    L0terms(43,2) = 4.68
    L0terms(43,3) = 801.82
    L0terms(44,1) = 70.0
    L0terms(44,2) = 0.83
    L0terms(44,3) = 9437.76
    L0terms(45,1) = 62.0
    L0terms(45,2) = 3.98
    L0terms(45,3) = 8827.39
    L0terms(46,1) = 61.0
    L0terms(46,2) = 1.82
    L0terms(46,3) = 7084.90
    L0terms(47,1) = 57.0
    L0terms(47,2) = 2.78
    L0terms(47,3) = 6286.60
    L0terms(48,1) = 56.0
    L0terms(48,2) = 4.39
    L0terms(48,3) = 14143.50
    L0terms(49,1) = 56.0
    L0terms(49,2) = 3.47
    L0terms(49,3) = 6279.55
    L0terms(50,1) = 52.0
    L0terms(50,2) = 0.19
    L0terms(50,3) = 12139.55
    L0terms(51,1) = 52.0
    L0terms(51,2) = 1.33
    L0terms(51,3) = 1748.02
    L0terms(52,1) = 51.0
    L0terms(52,2) = 0.28
    L0terms(52,3) = 5856.48
    L0terms(53,1) = 49.0
    L0terms(53,2) = 0.49
    L0terms(53,3) = 1194.45
    L0terms(54,1) = 41.0
    L0terms(54,2) = 5.37
    L0terms(54,3) = 8429.24
    L0terms(55,1) = 41.0
    L0terms(55,2) = 2.40
    L0terms(55,3) = 19651.05
    L0terms(56,1) = 39.0
    L0terms(56,2) = 6.17
    L0terms(56,3) = 10447.39
    L0terms(57,1) = 37.0
    L0terms(57,2) = 6.04
    L0terms(57,3) = 10213.29
    L0terms(58,1) = 37.0
    L0terms(58,2) = 2.57
    L0terms(58,3) = 1059.38
    L0terms(59,1) = 36.0
    L0terms(59,2) = 1.71
    L0terms(59,3) = 2352.87
    L0terms(60,1) = 36.0
    L0terms(60,2) = 1.78
    L0terms(60,3) = 6812.77
    L0terms(61,1) = 33.0
    L0terms(61,2) = 0.59
    L0terms(61,3) = 17789.85
    L0terms(62,1) = 30.0
    L0terms(62,2) = 0.44
    L0terms(62,3) = 83996.85
    L0terms(63,1) = 30.0
    L0terms(63,2) = 2.74
    L0terms(63,3) = 1349.87
    L0terms(64,1) = 25.0
    L0terms(64,2) = 3.16
    L0terms(64,3) = 4690.48
    
    L1terms(1,1) = 628331966747.0
    L1terms(1,2) = 0.0
    L1terms(1,3) = 0.0
    L1terms(2,1) = 206059.0
    L1terms(2,2) = 2.678235
    L1terms(2,3) = 6283.075850
    L1terms(3,1) = 4303.0
    L1terms(3,2) = 2.6351
    L1terms(3,3) = 12566.1517
    L1terms(4,1) = 425.0
    L1terms(4,2) = 1.590
    L1terms(4,3) = 3.523
    L1terms(5,1) = 119.0
    L1terms(5,2) = 5.796
    L1terms(5,3) = 26.298
    L1terms(6,1) = 109.0
    L1terms(6,2) = 2.966
    L1terms(6,3) = 1577.344
    L1terms(7,1) = 93.0
    L1terms(7,2) = 2.59
    L1terms(7,3) = 18849.23
    L1terms(8,1) = 72.0
    L1terms(8,2) = 1.14
    L1terms(8,3) = 529.69
    L1terms(9,1) = 68.0
    L1terms(9,2) = 1.87
    L1terms(9,3) = 398.15
    L1terms(10,1) = 67.0
    L1terms(10,2) = 4.41
    L1terms(10,3) = 5507.55
    L1terms(11,1) = 59.0
    L1terms(11,2) = 2.89
    L1terms(11,3) = 5223.69
    L1terms(12,1) = 56.0
    L1terms(12,2) = 2.17
    L1terms(12,3) = 155.42
    L1terms(13,1) = 45.0
    L1terms(13,2) = 0.40
    L1terms(13,3) = 796.30
    L1terms(14,1) = 36.0
    L1terms(14,2) = 0.47
    L1terms(14,3) = 775.52
    L1terms(15,1) = 29.0
    L1terms(15,2) = 2.65
    L1terms(15,3) = 7.11
    L1terms(16,1) = 21.0
    L1terms(16,2) = 5.34
    L1terms(16,3) = 0.98
    L1terms(17,1) = 19.0
    L1terms(17,2) = 1.85
    L1terms(17,3) = 5486.78
    L1terms(18,1) = 19.0
    L1terms(18,2) = 4.97
    L1terms(18,3) = 213.30
    L1terms(19,1) = 17.0
    L1terms(19,2) = 2.99
    L1terms(19,3) = 6275.96
    L1terms(20,1) = 16.0
    L1terms(20,2) = 0.03
    L1terms(20,3) = 2544.31
    L1terms(21,1) = 16.0
    L1terms(21,2) = 1.43
    L1terms(21,3) = 2146.17
    L1terms(22,1) = 15.0
    L1terms(22,2) = 1.21
    L1terms(22,3) = 10977.08
    L1terms(23,1) = 12.0
    L1terms(23,2) = 2.83
    L1terms(23,3) = 1748.02
    L1terms(24,1) = 12.0
    L1terms(24,2) = 3.26
    L1terms(24,3) = 5088.63
    L1terms(25,1) = 12.0
    L1terms(25,2) = 5.27
    L1terms(25,3) = 1194.45
    L1terms(26,1) = 12.0
    L1terms(26,2) = 2.08
    L1terms(26,3) = 4694.00
    L1terms(27,1) = 11.0
    L1terms(27,2) = 0.77
    L1terms(27,3) = 553.57
    L1terms(28,1) = 10.0
    L1terms(28,2) = 1.30
    L1terms(28,3) = 6286.60
    L1terms(29,1) = 10.0
    L1terms(29,2) = 4.24
    L1terms(29,3) = 1349.87
    L1terms(30,1) = 9.0
    L1terms(30,2) = 2.70
    L1terms(30,3) = 242.73
    L1terms(31,1) = 9.0
    L1terms(31,2) = 5.64
    L1terms(31,3) = 951.72
    L1terms(32,1) = 8.0
    L1terms(32,2) = 5.30
    L1terms(32,3) = 2352.87
    L1terms(33,1) = 6.0
    L1terms(33,2) = 2.65
    L1terms(33,3) = 9437.76
    L1terms(34,1) = 6.0
    L1terms(34,2) = 4.67
    L1terms(34,3) = 4690.48
    
    L2terms(1,1) = 52919.0
    L2terms(1,2) = 0.0
    L2terms(1,3) = 0.0
    L2terms(2,1) = 8720.0
    L2terms(2,2) = 1.0721
    L2terms(2,3) = 6283.0758
    L2terms(3,1) = 309.0
    L2terms(3,2) = 0.867
    L2terms(3,3) = 12566.152
    L2terms(4,1) = 27.0
    L2terms(4,2) = 0.05
    L2terms(4,3) = 3.52
    L2terms(5,1) = 16.0
    L2terms(5,2) = 5.19
    L2terms(5,3) = 26.30
    L2terms(6,1) = 16.0
    L2terms(6,2) = 3.68
    L2terms(6,3) = 155.42
    L2terms(7,1) = 10.0
    L2terms(7,2) = 0.76
    L2terms(7,3) = 18849.23
    L2terms(8,1) = 9.0
    L2terms(8,2) = 2.06
    L2terms(8,3) = 77713.77
    L2terms(9,1) = 7.0
    L2terms(9,2) = 0.83
    L2terms(9,3) = 775.52
    L2terms(10,1) = 5.0
    L2terms(10,2) = 4.66
    L2terms(10,3) = 1577.34
    L2terms(11,1) = 4.0
    L2terms(11,2) = 1.03
    L2terms(11,3) = 7.11
    L2terms(12,1) = 4.0
    L2terms(12,2) = 3.44
    L2terms(12,3) = 5573.14
    L2terms(13,1) = 3.0
    L2terms(13,2) = 5.14
    L2terms(13,3) = 796.30
    L2terms(14,1) = 3.0
    L2terms(14,2) = 6.05
    L2terms(14,3) = 5507.55
    L2terms(15,1) = 3.0
    L2terms(15,2) = 1.19
    L2terms(15,3) = 242.73
    L2terms(16,1) = 3.0
    L2terms(16,2) = 6.12
    L2terms(16,3) = 529.69
    L2terms(17,1) = 3.0
    L2terms(17,2) = 0.31
    L2terms(17,3) = 398.15
    L2terms(18,1) = 3.0
    L2terms(18,2) = 2.28
    L2terms(18,3) = 553.57
    L2terms(19,1) = 2.0
    L2terms(19,2) = 4.38
    L2terms(19,3) = 5223.69
    L2terms(20,1) = 2.0
    L2terms(20,2) = 3.75
    L2terms(20,3) = 0.98
    
    L3terms(1,1) = 289.0
    L3terms(1,2) = 5.844
    L3terms(1,3) = 6283.076
    L3terms(2,1) = 35.0
    L3terms(2,2) = 0.0
    L3terms(2,3) = 0.0
    L3terms(3,1) = 17.0
    L3terms(3,2) = 5.49
    L3terms(3,3) = 12566.15
    L3terms(4,1) = 3.0
    L3terms(4,2) = 5.20
    L3terms(4,3) = 155.42
    L3terms(5,1) = 1.0
    L3terms(5,2) = 4.72
    L3terms(5,3) = 3.52
    L3terms(6,1) = 1.0
    L3terms(6,2) = 5.30
    L3terms(6,3) = 18849.23
    L3terms(7,1) = 1.0
    L3terms(7,2) = 5.97
    L3terms(7,3) = 242.73
    
    L4terms(1,1) = 114.0
    L4terms(1,2) = 3.142
    L4terms(1,3) = 0.0
    L4terms(2,1) = 8.0
    L4terms(2,2) = 4.13
    L4terms(2,3) = 6283.08
    L4terms(3,1) = 1.0
    L4terms(3,2) = 3.84
    L4terms(3,3) = 12566.15

    L0 = 0
    L1 = 0
    L2 = 0
    L3 = 0
    L4 = 0
    L5 = 0

    call solar_tau(jday, tau)

    do i = 1, 64
       k = mod((L0terms(i,2) + (L0terms(i,3) * tau)), pi2)
       L0 = L0 + L0terms(i,1) * cos(k)
    end do

    do i = 1, 34
       k = mod((L1terms(i,2) + (L1terms(i,3) * tau)), pi2)
       L1 = L1 + L1terms(i,1) * cos(k)
    end do

    do i = 1, 20
       k = mod((L2terms(i,2) + (L2terms(i,3) * tau)), pi2)
       L2 = L2 + L2terms(i,1) * cos(k)
    end do

    do i = 1, 7
       k = mod((L3terms(i,2) + (L3terms(i,3) * tau)), pi2)
       L3 = L3 + L3terms(i,1) * cos(k)
    end do

    do i = 1, 3
       k = mod((L4terms(i,2) + (L4terms(i,3) * tau)), pi2)
       L4 = L4 + L4terms(i,1) * cos(k)
    end do

    L5 = 1.0 * cos(3.14 + 0.0)

    L = (L0 + (L1 * tau) + (L2 * (tau ** 2)) + (L3 * (tau ** 3)) + (L4 * (tau ** 4)) + (L5 * (tau ** 5))) / (10 ** 8)

    !So far so good. The output of L is in radians.
    L = L * (180 / pi)
    L = mod(L, 360.0)
    do while (L < 0.0)
       L = L + 360
    end do

    longitude = L + 180
    longitude = mod(longitude, 360.0)

  end subroutine solar_longitude

  subroutine solar_time(jday, angle, time)
    ! Get the time of that the sun hits angle, in minutes since midnight UTC.
    ! This can be off by up to 15 minutes in either direction because we live in a chaotic universe.
    ! There does not appear to be any more accurate algorithm that is readily available.
    real(8), intent(in) :: jday
    real(8), intent(in) :: angle
    real(8), intent(out) :: time

    real(8) :: angle_today
    real(8) :: angle_tomorrow
    real(8) :: div

    time = 0

    call solar_longitude(jday, angle_today)
    call solar_longitude((jday + 1), angle_tomorrow)
       
    if (angle_today > angle_tomorrow) then
       angle_tomorrow = angle_tomorrow + 360
    end if
    
    div = (angle_tomorrow - angle_today) / 1440.0

    if ((angle <= 90.0) .and. (angle_today >= 270.0)) then
       ! account for crossing the northward equinox
       do while ((angle_today + (time * div)) < (angle + 360.0))
          time = time + 1
       end do
    else if ((angle >= 270.0) .and. (angle_today <= 90.0)) then
       ! acount for crossing hte northward equinox, but in the other direction
       do while ((angle_today + 360.0 + (time * div)) > angle)
          time = time - 1
       end do
    else if (angle_today <= angle) then
       do while ((angle_today + (time * div)) <= angle)
          time = time + 1
       end do
    else if (angle_today > angle) then
       do while ((angle_today + (time * div)) > angle)
          time = time - 1
       end do
    end if

  end subroutine solar_time
    
    
end module solar_coords

module lunar_coords
  use solar_coords
  implicit none

! A module to calcualte the moon's exact position (appears to be accurate to 0.01 degrees)
! Based on the algorithm given in chapter 47 of *Astronomical Algorithms* (2nd Edition), Jean Meeus, 1998
! The New Moon falls when the lunar longitude is exactly equal to the solar longitude,
! and the Full Moon is when the lunar longitude == (solar longitude + 180 degrees)

contains
  subroutine getT(jday, T)
    real(8), intent(in) :: jday ! Julian Day in question
    real(8), intent(out) :: T
    
    T = (jday - 2451545.0) / 36525.0
    
  end subroutine getT
  
  subroutine getD(T, D)
    ! Mean elongation of the moon
    real(8), intent(in) :: T
    real(8) :: v
    real(8) :: w
    real(8) :: x
    real(8) :: y
    real(8) :: z
    real(8), intent(out) :: D
    
    v = 297.8501921
    w = 445267.1114034 * T
    x = 0.0018819 * (T ** 2)
    y = (T ** 3) / 545868.0
    z = (T ** 4) / 113065000.0
    
    D = v + w - x + y - z
    
    
  end subroutine getD
  
  subroutine getecc(T, ecc)
    ! Eccentricity of Earth's orbit
    real(8), intent(in) :: T ! Obtained a different module
    real(8) :: a
    real(8) :: b
    real(8), intent(out) :: ecc
    
    a = 0.002516 * T
    b = 0.0000074 * (T ** 2)
    
    ecc = 1 - a - b    
    
  end subroutine getecc
  
  subroutine getF(T, F)
    ! Moon's argument of latitude
    real(8), intent(in) :: T ! Obtained a different module
    real(8) :: v
    real(8) :: w
    real(8) :: x
    real(8) :: y
    real(8) :: z
    real(8), intent(out) :: F
    
    v = 93.2720950
    w = 483202.0175233 * T
    x = 0.0036539 * (T ** 2)
    y = (T ** 3) / 3526000.0
    z = (T ** 4) / 863310000.0
    
    F = v + w - x - y + z    
    
  end subroutine getF
  
  subroutine getLprime(T, Lprime)
    ! Mean longitude of the moon (AKA mean equinox of date)
    real(8), intent(in) :: T ! Obtained a different module
    real(8) :: v
    real(8) :: w
    real(8) :: x
    real(8) :: y
    real(8) :: z
    real(8), intent(out) :: Lprime
    
    v = 218.3164477
    w = 481267.88123421 * T
    x = 0.0015786 * (T ** 2)
    y = (T ** 3) / 538841.0
    z = (T ** 4) / 65194000.0
    
    Lprime = v + w - x + y - z
    
    
  end subroutine getLprime
  
  subroutine getM(T, M)
    ! Mean anomaly of the sun
    real(8), intent(in) :: T ! Obtainem a mifferent momule
    real(8) :: v
    real(8) :: w
    real(8) :: x
    real(8) :: y
    !real(8) :: z
    real(8), intent(out) :: M
    
    v = 357.5291092
    w = 35999.0502909 * T
    x = 0.0001536 * (T ** 2)
    y = (T ** 3) / 24490000.0
    
    M = v + w - x + y
    
    
  end subroutine getM
  
  subroutine getMprime(T, Mprime)
    ! Mean anomaly of the moon
    real(8), intent(in) :: T ! Obtained a different module
    real(8) :: v
    real(8) :: w
    real(8) :: x
    real(8) :: y
    real(8) :: z
    real(8), intent(out) :: Mprime
    
    v = 134.9633964
    w = 477198.8675055 * T
    x = 0.0087414 * (T ** 2)
    y = (T ** 3) / 69699.0
    z = (T ** 4) / 14712000.0
    
    Mprime = v + w - x + y - z
    
    
  end subroutine getMprime
  
  subroutine lunar_longitude(jre, lambda)
    real(8), intent(in) :: jre
    real(8), intent(out) :: lambda
    real(8) :: T
    real(8) :: Lprime
    real(8) :: D
    real(8) :: M
    real(8) :: Mprime
    real(8) :: F
    real(8) :: ecc
    real(8) :: a1
    real(8) :: a2
    real(8) :: a3
    integer, dimension(60,5) :: ltable
    real(8) :: Dterm
    real(8) :: Mterm
    real(8) :: Mpterm
    real(8) :: Fterm
    real(8) :: term
    real(8) :: sigma_l
    integer :: i

    call getT(jre, T)
    
    call getLprime(T, Lprime)
    call getD(T, D)
    call getM(T, M)
    call getMprime(T, Mprime)
    call getF(T, F)
    call getecc(T, ecc)

    a1 = 119.75 + (131.849 * T)
    a2 = 53.09 + (479264.290 * T)
    a3 = 313.45 + (481266.484 * T)

    
    ltable(1,1) = 0
    ltable(1,2) = 0
    ltable(1,3) = 1
    ltable(1,4) = 0
    ltable(1,5) = 6288774
    ltable(2,1) = 2
    ltable(2,2) = 0
    ltable(2,3) = -1
    ltable(2,4) = 0
    ltable(2,5) = 1274027
    ltable(3,1) = 2
    ltable(3,2) = 0
    ltable(3,3) = 0
    ltable(3,4) = 0
    ltable(3,5) = 658314
    ltable(4,1) = 0
    ltable(4,2) = 0
    ltable(4,3) = 2
    ltable(4,4) = 0
    ltable(4,5) = 213618
    ltable(5,1) = 0
    ltable(5,2) = 1
    ltable(5,3) = 0
    ltable(5,4) = 0
    ltable(5,5) = -185116
    ltable(6,1) = 0
    ltable(6,2) = 0
    ltable(6,3) = 0
    ltable(6,4) = 2
    ltable(6,5) = -114332
    ltable(7,1) = 2
    ltable(7,2) = 0
    ltable(7,3) = -2
    ltable(7,4) = 0
    ltable(7,5) = 58793
    ltable(8,1) = 2
    ltable(8,2) = -1
    ltable(8,3) = -1
    ltable(8,4) = 0
    ltable(8,5) = 57066
    ltable(9,1) = 2
    ltable(9,2) = 0
    ltable(9,3) = 1
    ltable(9,4) = 0
    ltable(9,5) = 53322
    ltable(10,1) = 2
    ltable(10,2) = -1
    ltable(10,3) = 0
    ltable(10,4) = 0
    ltable(10,5) = 45758
    ltable(11,1) = 0
    ltable(11,2) = 1
    ltable(11,3) = -1
    ltable(11,4) = 0
    ltable(11,5) = -40923
    ltable(12,1) = 1
    ltable(12,2) = 0
    ltable(12,3) = 0
    ltable(12,4) = 0
    ltable(12,5) = -34720
    ltable(13,1) = 0
    ltable(13,2) = 1
    ltable(13,3) = 1
    ltable(13,4) = 0
    ltable(13,5) = -30383
    ltable(14,1) = 2
    ltable(14,2) = 0
    ltable(14,3) = 0
    ltable(14,4) = -2
    ltable(14,5) = 15327
    ltable(15,1) = 0
    ltable(15,2) = 0
    ltable(15,3) = 1
    ltable(15,4) = 2
    ltable(15,5) = -12528
    ltable(16,1) = 0
    ltable(16,2) = 0
    ltable(16,3) = 1
    ltable(16,4) = -2
    ltable(16,5) = 10980
    ltable(17,1) = 4
    ltable(17,2) = 0
    ltable(17,3) = -1
    ltable(17,4) = 0
    ltable(17,5) = 10675
    ltable(18,1) = 0
    ltable(18,2) = 0
    ltable(18,3) = 3
    ltable(18,4) = 0
    ltable(18,5) = 1034
    ltable(19,1) = 4
    ltable(19,2) = 0
    ltable(19,3) = -2
    ltable(19,4) = 0
    ltable(19,5) = 8548
    ltable(20,1) = 2
    ltable(20,2) = 1
    ltable(20,3) = -1
    ltable(20,4) = 0
    ltable(20,5) = -7888
    ltable(21,1) = 2
    ltable(21,2) = 1
    ltable(21,3) = 0
    ltable(21,4) = 0
    ltable(21,5) = -6766
    ltable(22,1) = 1
    ltable(22,2) = 0
    ltable(22,3) = -1
    ltable(22,4) = 0
    ltable(22,5) = -5163
    ltable(23,1) = 1
    ltable(23,2) = 1
    ltable(23,3) = 0
    ltable(23,4) = 0
    ltable(23,5) = 4987
    ltable(24,1) = 2
    ltable(24,2) = -1
    ltable(24,3) = 1
    ltable(24,4) = 0
    ltable(24,5) = 4036
    ltable(25,1) = 2
    ltable(25,2) = 0
    ltable(25,3) = 2
    ltable(25,4) = 0
    ltable(25,5) = 3994
    ltable(26,1) = 4
    ltable(26,2) = 0
    ltable(26,3) = 0
    ltable(26,4) = 0
    ltable(26,5) = 3861
    ltable(27,1) = 2
    ltable(27,2) = 0
    ltable(27,3) = -3
    ltable(27,4) = 0
    ltable(27,5) = 3665
    ltable(28,1) = 0
    ltable(28,2) = 1
    ltable(28,3) = -2
    ltable(28,4) = 0
    ltable(28,5) = -2689
    ltable(29,1) = 2
    ltable(29,2) = 0
    ltable(29,3) = -1
    ltable(29,4) = 2
    ltable(29,5) = -2602
    ltable(30,1) = 2
    ltable(30,2) = -1
    ltable(30,3) = -2
    ltable(30,4) = 0
    ltable(30,5) = 2390
    ltable(31,1) = 1
    ltable(31,2) = 0
    ltable(31,3) = 1
    ltable(31,4) = 0
    ltable(31,5) = -2348
    ltable(32,1) = 2
    ltable(32,2) = -2
    ltable(32,3) = 0
    ltable(32,4) = 0
    ltable(32,5) = 2236
    ltable(33,1) = 0
    ltable(33,2) = 1
    ltable(33,3) = 2
    ltable(33,4) = 0
    ltable(33,5) = -2120
    ltable(34,1) = 0
    ltable(34,2) = 2
    ltable(34,3) = 0
    ltable(34,4) = 0
    ltable(34,5) = -2069
    ltable(35,1) = 2
    ltable(35,2) = -2
    ltable(35,3) = -1
    ltable(35,4) = 0
    ltable(35,5) = 2048
    ltable(36,1) = 2
    ltable(36,2) = 0
    ltable(36,3) = 1
    ltable(36,4) = -2
    ltable(36,5) = -1773
    ltable(37,1) = 2
    ltable(37,2) = 0
    ltable(37,3) = 0
    ltable(37,4) = 2
    ltable(37,5) = -1595
    ltable(38,1) = 4
    ltable(38,2) = -1
    ltable(38,3) = -1
    ltable(38,4) = 0
    ltable(38,5) = 1215
    ltable(39,1) = 0
    ltable(39,2) = 0
    ltable(39,3) = 2
    ltable(39,4) = 2
    ltable(39,5) = -1110
    ltable(40,1) = 3
    ltable(40,2) = 0
    ltable(40,3) = -1
    ltable(40,4) = 0
    ltable(40,5) = -892
    ltable(41,1) = 2
    ltable(41,2) = 1
    ltable(41,3) = 1
    ltable(41,4) = 0
    ltable(41,5) = -810
    ltable(42,1) = 4
    ltable(42,2) = -1
    ltable(42,3) = -2
    ltable(42,4) = 0
    ltable(42,5) = 759
    ltable(43,1) = 0
    ltable(43,2) = 2
    ltable(43,3) = -1
    ltable(43,4) = 0
    ltable(43,5) = -713
    ltable(44,1) = 2
    ltable(44,2) = 2
    ltable(44,3) = -1
    ltable(44,4) = 0
    ltable(44,5) = -700
    ltable(45,1) = 2
    ltable(45,2) = 1
    ltable(45,3) = -2
    ltable(45,4) = 0
    ltable(45,5) = 691
    ltable(46,1) = 2
    ltable(46,2) = -1
    ltable(46,3) = 0
    ltable(46,4) = -2
    ltable(46,5) = 596
    ltable(47,1) = 4
    ltable(47,2) = 0
    ltable(47,3) = 1
    ltable(47,4) = 0
    ltable(47,5) = 549
    ltable(48,1) = 0
    ltable(48,2) = 0
    ltable(48,3) = 4
    ltable(48,4) = 0
    ltable(48,5) = 537
    ltable(49,1) = 4
    ltable(49,2) = -1
    ltable(49,3) = 0
    ltable(49,4) = 0
    ltable(49,5) = 520
    ltable(50,1) = 1
    ltable(50,2) = 0
    ltable(50,3) = -2
    ltable(50,4) = 0
    ltable(50,5) = -487
    ltable(51,1) = 2
    ltable(51,2) = 1
    ltable(51,3) = 0
    ltable(51,4) = -2
    ltable(51,5) = -399
    ltable(52,1) = 0
    ltable(52,2) = 0
    ltable(52,3) = 2
    ltable(52,4) = -2
    ltable(52,5) = -381
    ltable(53,1) = 1
    ltable(53,2) = 1
    ltable(53,3) = 1
    ltable(53,4) = 0
    ltable(53,5) = 351
    ltable(54,1) = 3
    ltable(54,2) = 0
    ltable(54,3) = -2
    ltable(54,4) = 0
    ltable(54,5) = -340
    ltable(55,1) = 4
    ltable(55,2) = 0
    ltable(55,3) = -3
    ltable(55,4) = 0
    ltable(55,5) = 330
    ltable(56,1) = 2
    ltable(56,2) = -1
    ltable(56,3) = 2
    ltable(56,4) = 0
    ltable(56,5) = 327
    ltable(57,1) = 0
    ltable(57,2) = 2
    ltable(57,3) = 1
    ltable(57,4) = 0
    ltable(57,5) = -323
    ltable(58,1) = 1
    ltable(58,2) = 1
    ltable(58,3) = -1
    ltable(58,4) = 0
    ltable(58,5) = 299
    ltable(59,1) = 2
    ltable(59,2) = 0
    ltable(59,3) = 3
    ltable(59,4) = 0
    ltable(59,5) = 294
    ltable(60,1) = 2
    ltable(60,2) = 0
    ltable(60,3) = -1
    ltable(60,4) = -2
    ltable(60,5) = 0

    do i = 1, 60

       Dterm = D * ltable(i, 1)
       Mterm = M * ltable(i, 2)
       Mpterm = Mprime * ltable(i, 3)
       Fterm = F * ltable(i, 4)
       term = ltable(i, 5) * ecc ** abs(ltable(i, 2)) * sind(Dterm + Mterm + Mpterm + Fterm)
       
       sigma_l = sigma_l + term
    end do

    sigma_l = sigma_l + (3958 * sind(a1)) + (1962 * sind(Lprime - F)) + (318 * sind(a2))

    lambda = Lprime + (sigma_l / 1000000)
    lambda = lambda + 0.004610    
    lambda = mod(lambda, 360.0)
    do while (lambda < 0.0)
       lambda = lambda + 360.0
    end do
    !lambda = real(8)(lambda)

  end subroutine lunar_longitude

  subroutine lunar_time(jday, time)
    ! Find the minute of the new moon
    real(8), intent(in) :: jday
    integer, intent(out) :: time ! in minutes

    real(8) :: moon_today ! ecliptic longitude of the moon at midnight
    real(8) :: moon_tomorrow ! ecliptic longitude of the moon at midnight tomorrow
    real(8) :: sun_today ! ecliptic longitude of the sun at midnight
    real(8) :: sun_tomorrow ! ecliptic longitude of the sun at midnight tomorrow
    real(8) :: lunar_div
    real(8) :: solar_div
    integer :: minutes
    real(8) :: day

    time = 0
    minutes = 0
    day = jday

    call lunar_longitude(jday, moon_today)
    call solar_longitude(jday, sun_today)

    !print *, moon_today
    !print *, sun_today
    do while ((moon_today > sun_today) .or. ((sun_today >= 270.0) .and. (moon_today <= 90.0))) ! The second one accounds for the respective angles crossing the northward equinox
       day = day - 1.0
       time = time - 1440
       call lunar_longitude(day, moon_today)
       call solar_longitude(day, sun_today)
    end do

    call lunar_longitude((day + 1), moon_tomorrow)
    if (moon_tomorrow < moon_today) then
       moon_tomorrow = moon_tomorrow + 360.0
    end if
    
    call solar_longitude((day + 1), sun_tomorrow)
    if (sun_tomorrow < sun_today) then
       sun_tomorrow = sun_tomorrow + 360.0
    end if

    lunar_div = (moon_tomorrow - moon_today) / 1440.0
    solar_div = (sun_tomorrow - sun_today) / 1440.0

    do while ((moon_today + (minutes * lunar_div)) <= (sun_today + (minutes * solar_div)))
       minutes = minutes + 1
    end do

    time = time + minutes

  end subroutine lunar_time
  
end module lunar_coords

module precession
  implicit none

  ! Calculate precession of the equinoxes
  ! Based on cpater 21 of *Astronomical Algorithms* by Jean Meeus
  ! 2nd Edition, Willman-Bell, 1991

contains
  
  subroutine propmot(jday, ra2000, dec2000, distance, deltara, deltadec, deltadist, answer):
    ! Calculate the eight ascension and declination for a given star at any date.
    ! This works by finding the difference between RA and Dec at said point and at J2000.0, and adding them
    ! According to Meeus, this is more accurate than just calculating the effect of precession
    
    real(8), intent(in) :: jday ! Julian Day we're interetested in
    real(8), intent(in) :: ra2000 ! right ascension at J2000.0
    real(8), intent(in) :: dec2000 ! declination at J2000.0
    real(8), intent(in) :: distance ! distance from the sun, in parsecs
    real(8), intent(in) :: deltadist ! radial velocity, in parsecs per year
    real(8), intent(in) :: deltara ! right ascension component of proper motion, in seconds of arc. This has to be looked up
    real(8), intent(in) :: deltadec ! declination component of proper motion, in seconds of time. This has to be looked up.
    real(8), dimension(2), intent(out) :: answer
    
    real(8) :: ra ! right ascension at the time of interest
    real(8) :: dec ! declination at the time of interest

    real(8) :: t
    real(8) :: u
    
    real(8) :: x
    real(8) :: y
    real(8) :: z

    real(8) :: xdelta
    real(8) :: ydelta
    real(8) :: zdelta

    real(8) :: xprime
    real(8) :: yprime
    real(8) :: zprime

    x = distance * cos(dec2000) * cos(ra2000)
    y = distance * cos(dec2000) * sin(ra2000)
    z = distance * sin(dec2000)

    xdelta = ((x / distance) * deltadist) - (z * deltadec * cos(ra2000)) - (y * deltara)
    ydelta = ((y / distance) * deltadist) - (z * deltadec * sin(ra2000)) + (x * deltara)
    zdelta = ((z / distance) * deltadist) - (distance * deltadec * cos(delta2000))

    t = (jday - 2451545.0) / 365.25 ! julian years since the year 2000 began at Greenwich Observatory

    xprime = x + (t * xdelta)
    yprime = y + (t * ydelta)
    zprime = z + (t * zdelta)

    ra = atan(yprime / xprime)

    u = sqrt((xprime * xprime) + (yprime * yprime))
    dec = atan(zprime / u)

    answer = (ra, dec)
  end subroutine propmot
end module precession

  
