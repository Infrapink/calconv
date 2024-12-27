module stellar_coords
  implicit none

  ! Calculate right ascension and declination of a given star,
  ! taking into account its proper motion and the precession of the equinoxes
  
  ! Based on cpater 21 of *Astronomical Algorithms* by Jean Meeus
  ! 2nd Edition, Willman-Bell, 1991
contains
  subroutine propmot(jday, ra2000, dec2000, distance, rv, deltara, deltadec, answer)
    ! Calculate the effect of proper motion on a star's right ascension and declination
    
    double precision, intent(in) :: jday ! Julian Day we're interetested in
    double precision, intent(in) :: ra2000 ! right ascension at J2000.0
    double precision, intent(in) :: dec2000 ! declination at J2000.0
    double precision, intent(in) :: distance ! distance from the sun, in parsecs
    double precision, intent(in) :: rv ! radial velocity, in parsecs per year
    double precision, intent(in) :: deltara ! right ascension component of proper motion, in seconds of arc. This has to be looked up
    double precision, intent(in) :: deltadec ! declination component of proper motion, in seconds of time. This has to be looked up.
    double precision, dimension(2), intent(out) :: answer
    
    double precision :: ra ! right ascension at the time of interest
    double precision :: dec ! declination at the time of interest

    double precision :: t
    double precision :: u
    
    double precision :: x
    double precision :: y
    double precision :: z

    double precision :: xdelta
    double precision :: ydelta
    double precision :: zdelta

    double precision :: xprime
    double precision :: yprime
    double precision :: zprime

    double precision :: pi
    double precision :: d2r ! convert degrees to radians
    double precision :: r2d ! convert radians to degrees

    !print *, "rv = ", rv
    !print *, "deltara = ", deltara
    !print *, "deltadec = ", deltadec

    pi = 4.0 * atan(1.0)
    d2r = pi / 180.0 ! convert degrees to radians
    r2d = 180.0 / pi ! convert radians to degrees

    x = distance * cos(dec2000 * d2r) * cos(ra2000 * d2r)
    y = distance * cos(dec2000 * d2r) * sin(ra2000 * d2r)
    z = distance * sin(dec2000 * d2r)
    !print *, x, y, z

    xdelta = ((x / distance) * rv) - (z * deltadec * cos(ra2000 * d2r)) - (y * deltara)
    ydelta = ((y / distance) * rv) - (z * deltadec * sin(ra2000 * d2r)) + (x * deltara)
    zdelta = ((z / distance) * rv) - (distance * deltadec * cos(dec2000 * d2r))

    t = (jday - 2451545.0) / 365.25 ! julian years since the year 2000 began at Greenwich Observatory

    xprime = x + (t * xdelta)
    yprime = y + (t * ydelta)
    zprime = z + (t * zdelta)

    ra = r2d * atan(yprime / xprime)
    !print *, "ra1 = ", ra * r2d
    !print *, "fraction = ", (yprime / xprime)
    ! now to account for trrgonometric trickiness
    if ((yprime / xprime) >= 0) then
       if ((ra2000 <= 135.0) .or. (ra2000 >= 315.0)) then ! ra in ALL quadrant
          ra = 0 + ra
       else ! ra in TAN quadrant
          ra = 180.0 + ra
       end if
    else if ((yprime / xprime) < 0) then
       if ((ra2000 >= 45.0) .and. (ra2000 <= 225.0)) then ! ra in SIN quadrant
          ra = 180.0 + ra
       else ! ra in COS quadrant
          ra = 360.0 + ra
       end if
    end if
    
    !print *, "y' = ", yprime
    !print *, "ra2 = ", ra
    !print *, "sin(ra) = ", sin(d2r * ra)
    !print *, "x' = ", xprime

    u = sqrt((xprime * xprime) + (yprime * yprime))
    dec = atan(zprime / u) * r2d

    !print *, ra
    !print *, dec
    !print *, "BEGIN PROPMOT"
    !print *, ra2000
    !print *, ra
    !print *, "END PROPMOT"
    answer(1) = ra
    answer(2) = dec
    !print *, answer
  end subroutine propmot

  subroutine nutation(jday, nut)
    ! Calculate the nutation of the obliquity to the ecplitic
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, dimension(0:2), intent(out) :: nut ! Nutation to the ecliptic and of longitude

    double precision :: T ! Julian Centuries since J2000.0
    double precision :: D ! mean elonation of the moon from the sun
    double precision :: M ! mean anomaly of the sun
    double precision :: Mprime ! mean anomaly of the moon
    double precision :: F ! moon's argument of latitude
    double precision :: omega ! longitude of the ascending node of the moon's mean orbit on the ecliptic

    !double precision, dimension(64,5) :: args
    !double precision, dimension(64,2) :: psi_coeffs
    !double precision, dimension(64,2) :: eps_coeffs
    double precision, dimension(63,9) :: deltable
    double precision :: epsilon0 !mean obliquity of the ecliptic, in degrees
    double precision :: delta_epsilon ! variation in the obliquity of the ecliptic, in arcseconds
    double precision :: delta_psi ! nutation in longitude, in arcseconds
    double precision :: U ! Julian Decamillennia since J2000.0

    integer :: i
    double precision :: a ! placeholder

    double precision :: pi
    double precision :: d2r ! convert degrees to radians
    double precision :: r2d ! convert radians to degrees

    pi = 4.0 * atan(1.0)
    r2d = 180.0 / pi
    d2r = pi / 180.0

    T = (jday - 2451545.0) / 36525.0
    D = 297.85036 + (445267.111480 * T) - (0.00191427 * T * T) + ((T ** 3) / 189474.0)
    M = 357.52772 + (35999.050340 * T) - (0.0001603 * T * T) - ((T ** 3) / 300000.0)
    Mprime = 134.96298 + (477198.867398 * T) + (0.0086972 * T * T) + ((T ** 3) / 56250.0)
    F = 93.27191 + (483202.017538 * T) - (0.0036825 * T * T) + ((T ** 3) / 327270.0)
    omega = 125.04452 - (1934.136261 * T) + (0.0020708 * T * T) + ((T ** 3) / 450000.0)

    ! now for deltable
    ! See Meeus, pp. 145 - 146
    deltable( 1,:) = [ 0.0,  0.0,  0.0,  0.0, 1.0, -171996.0, -174.2, 92025.0,  8.9]
    deltable( 2,:) = [-2.0,  0.0,  0.0,  2.0, 2.0,  -13187.0,   -1.6,  5736.0, -3.1]
    deltable( 3,:) = [ 0.0,  0.0,  0.0,  2.0, 2.0,   -2274.0,   -0.2,   977.0, -0.5]
    deltable( 4,:) = [ 0.0,  0.0,  0.0,  0.0, 2.0,    2062.0,    0.2,  -895.0,  0.5]
    deltable( 5,:) = [ 0.0,  1.0,  0.0,  0.0, 0.0,    1426.0,   -3.4,    54.0, -0.1]
    deltable( 6,:) = [ 0.0,  0.0,  1.0,  0.0, 0.0,     712.0,    0.1,    -7.0,  0.0]
    deltable( 7,:) = [-2.0,  1.0,  0.0,  2.0, 2.0,    -517.0,    1.2,   224.0, -0.6]
    deltable( 8,:) = [ 0.0,  0.0,  0.0,  2.0, 1.0,    -386.0,   -0.4,   200.0,  0.0]
    deltable( 9,:) = [ 0.0,  0.0,  1.0,  2.0, 2.0,    -301.0,    0.0,   129.0, -0.1]
    deltable(10,:) = [-2.0, -1.0,  0.0,  2.0, 2.0,     217.0,   -0.5,   -95.0,  0.3]
    deltable(11,:) = [-2.0,  0.0,  1.0,  0.0, 0.0,    -158.0,    0.0,     0.0,  0.0]
    deltable(12,:) = [-2.0,  0.0,  0.0,  2.0, 1.0,     129.0,    0.1,   -70.0,  0.0]
    deltable(13,:) = [ 0.0,  0.0, -1.0,  2.0, 2.0,     123.0,    0.0,   -53.0,  0.0]
    deltable(14,:) = [ 2.0,  0.0,  0.0,  0.0, 0.0,      63.0,    0.0,     0.0,  0.0]
    deltable(15,:) = [ 0.0,  0.0,  1.0,  0.0, 1.0,      63.0,    0.1,   -35.0,  0.0]
    deltable(16,:) = [ 2.0,  0.0, -1.0,  2.0, 2.0,     -59.0,    0.0,    26.0,  0.0]
    deltable(17,:) = [ 0.0,  0.0, -1.0,  0.0, 1.0,     -58.0,   -0.1,    32.0,  0.0]
    deltable(18,:) = [ 0.0,  0.0,  1.0,  2.0, 1.0,     -51.0,    0.0,    27.0,  0.0]
    deltable(19,:) = [-2.0,  0.0,  2.0,  0.0, 0.0,      48.0,    0.0,     0.0,  0.0]
    deltable(20,:) = [ 0.0,  0.0, -2.0,  2.0, 1.0,      46.0,    0.0,   -24.0,  0.0]
    deltable(21,:) = [ 2.0,  0.0,  0.0,  2.0, 2.0,     -38.0,    0.0,    16.0,  0.0]
    deltable(22,:) = [ 0.0,  0.0,  2.0,  2.0, 2.0,     -31.0,    0.0,    13.0,  0.0]
    deltable(23,:) = [ 0.0,  0.0,  2.0,  0.0, 0.0,      29.0,    0.0,     0.0,  0.0]
    deltable(24,:) = [-2.0,  0.0,  1.0,  2.0, 2.0,      29.0,    0.0,   -12.0,  0.0]
    deltable(25,:) = [ 0.0,  0.0,  2.0,  2.0, 0.0,      26.0,    0.0,     0.0,  0.0]
    deltable(26,:) = [-2.0,  0.0,  0.0,  2.0, 0.0,     -22.0,    0.0,     0.0,  0.0]
    deltable(27,:) = [ 0.0,  0.0, -1.0,  2.0, 1.0,      21.0,    0.0,   -10.0,  0.0]
    deltable(28,:) = [ 0.0,  2.0,  0.0,  0.0, 0.0,      17.0,   -0.1,     0.0,  0.0]
    deltable(29,:) = [ 2.0,  0.0, -1.0,  0.0, 1.0,      16.0,    0.0,    -8.0,  0.0]
    deltable(30,:) = [-2.0,  2.0,  0.0,  2.0, 2.0,     -16.0,    0.1,     7.0,  0.0]
    deltable(31,:) = [ 0.0,  1.0,  0.0,  0.0, 1.0,      15.0,    0.0,     9.0,  0.0]
    deltable(32,:) = [-2.0,  0.0,  1.0,  0.0, 1.0,     -13.0,    0.0,     7.0,  0.0]
    deltable(33,:) = [ 0.0, -1.0,  0.0,  0.0, 1.0,     -12.0,    0.0,     6.0,  0.0]
    deltable(34,:) = [ 0.0,  0.0,  2.0, -2.0, 0.0,      11.0,    0.0,     0.0,  0.0]
    deltable(35,:) = [ 2.0,  0.0, -1.0,  2.0, 1.0,     -10.0,    0.0,     5.0,  0.0]
    deltable(36,:) = [ 2.0,  0.0,  1.0,  2.0, 2.0,      -8.0,    0.0,     3.0,  0.0]
    deltable(37,:) = [ 0.0,  1.0,  0.0,  2.0, 2.0,       7.0,    0.0,    -3.0,  0.0]
    deltable(38,:) = [-2.0,  1.0,  1.0,  0.0, 0.0,      -7.0,    0.0,     0.0,  0.0]
    deltable(39,:) = [ 0.0, -1.0,  0.0,  2.0, 2.0,      -7.0,    0.0,     3.0,  0.0]
    deltable(40,:) = [ 2.0,  0.0,  0.0,  2.0, 1.0,      -7.0,    0.0,     3.0,  0.0]
    deltable(41,:) = [ 2.0,  0.0,  1.0,  0.0, 0.0,       6.0,    0.0,     0.0,  0.0]
    deltable(42,:) = [-2.0,  0.0,  2.0,  2.0, 2.0,       6.0,    0.0,    -3.0,  0.0]
    deltable(43,:) = [-2.0,  0.0,  1.0,  2.0, 1.0,       6.0,    0.0,    -3.0,  0.0]
    deltable(44,:) = [ 2.0,  0.0, -2.0,  0.0, 1.0,      -6.0,    0.0,     3.0,  0.0]
    deltable(45,:) = [ 2.0,  0.0,  0.0,  0.0, 1.0,      -6.0,    0.0,     3.0,  0.0]
    deltable(46,:) = [ 0.0, -1.0,  1.0,  0.0, 0.0,       5.0,    0.0,     0.0,  0.0]
    deltable(47,:) = [-2.0, -1.0,  0.0,  2.0, 1.0,      -5.0,    0.0,     3.0,  0.0]
    deltable(48,:) = [-2.0,  0.0,  0.0,  0.0, 1.0,      -5.0,    0.0,     3.0,  0.0]
    deltable(49,:) = [ 0.0,  0.0,  2.0,  2.0, 1.0,      -5.0,    0.0,     3.0,  0.0]
    deltable(50,:) = [-2.0,  0.0,  2.0,  0.0, 1.0,       4.0,    0.0,     0.0,  0.0]
    deltable(51,:) = [-2.0,  1.0,  0.0,  2.0, 1.0,       4.0,    0.0,     0.0,  0.0]
    deltable(52,:) = [ 0.0,  0.0,  1.0, -2.0, 0.0,       4.0,    0.0,     0.0,  0.0]
    deltable(53,:) = [-1.0,  0.0,  1.0,  0.0, 0.0,      -4.0,    0.0,     0.0,  0.0]
    deltable(54,:) = [-2.0,  1.0,  0.0,  0.0, 0.0,      -4.0,    0.0,     0.0,  0.0]
    deltable(55,:) = [ 1.0,  0.0,  0.0,  0.0, 0.0,      -4.0,    0.0,     0.0,  0.0]
    deltable(56,:) = [ 0.0,  0.0,  1.0,  2.0, 0.0,       3.0,    0.0,     0.0,  0.0]
    deltable(57,:) = [ 0.0,  0.0, -2.0,  2.0, 2.0,      -3.0,    0.0,     0.0,  0.0]
    deltable(58,:) = [-1.0, -1.0,  1.0,  0.0, 0.0,      -3.0,    0.0,     0.0,  0.0]
    deltable(59,:) = [ 0.0,  1.0,  1.0,  0.0, 1.0,      -3.0,    0.0,     0.0,  0.0]
    deltable(60,:) = [ 0.0, -1.0,  1.0,  2.0, 2.0,      -3.0,    0.0,     0.0,  0.0]
    deltable(61,:) = [ 2.0, -1.0, -1.0,  2.0, 2.0,      -3.0,    0.0,     0.0,  0.0]
    deltable(62,:) = [ 0.0,  0.0,  3.0,  2.0, 2.0,      -3.0,    0.0,     0.0,  0.0]
    deltable(63,:) = [ 2.0, -1.0,  0.0,  2.0, 2.0,      -3.0,    0.0,     0.0,  0.0]

    delta_epsilon = 0.0 ! nutation in obliquity, at this point in tenths of milliarcseconds
    delta_psi     = 0.0 ! nutation in longitude, at this point in tenths of milliarcseconds
    do i = 1, 63
       delta_psi     = delta_psi     + ( (deltable(i,6) + (T * deltable(i,7))) * dsind( (D * deltable(i,1)) + (M * deltable(i,2)) + (Mprime * deltable(i,3)) + (F * deltable(i, 4)) + (omega * deltable(i, 5)) ) )
       delta_epsilon = delta_epsilon + ( (deltable(i,8) + (T * deltable(i,9))) * dcosd( (D * deltable(i,1)) + (M * deltable(i,2)) + (Mprime * deltable(i,3)) + (F * deltable(i, 4)) + (omega * deltable(i, 5)) ) )
       
       !a = d2r * ((args(i,1) * D) + (args(i,2) * M) + (args(i,3) * Mprime) + (args(i,4) * F) + (args(i,5) * omega))
       !delta_epsilon = delta_epsilon + ((eps_coeffs(i,1) + (T * eps_coeffs(i,2))) * cos(a))
       !delta_psi = delta_psi + ((psi_coeffs(i,1) + (T * psi_coeffs(i,2))) * sin(a))


       
       !a = (eps_coeffs(i,1) + (eps_coeffs(i,2) * T))
       !a = a * cos(d2r * ((args(i,1) * D) + (args(i,2) * M) + (args(i,3) * Mprime) + (args(i,4) * F) + (args(i,5) * omega)))
       !delta_epsilon = delta_epsilon + a

       !a =  args(i,1) * D
       !a = a + (args(i,2) * M)
       !a = a + (args(i,3) * Mprime)
       !a = a + (args(i,4) * F)
       !a = a + (args(i,5) * omega)
       !a = sin(d2r * a)
       !a = a * (eps_coeffs(i,1) + (eps_coeffs(i,2) * T))
    end do

    delta_epsilon = delta_epsilon / 10000.0 ! convert to arcseconds
    delta_psi = delta_psi / 10000.0 ! convert to arcseconds
    delta_epsilon = delta_epsilon / 3600.0 ! convert delta_epsilon into degrees
    delta_psi = delta_psi / 3600.0 ! convert delta_psi into degrees

    ! Laskar's method for making this algorithm accurate over many millennia
    U = T / 100.0
    a = 0.0
    !epsilon0 = (23.0 * 360.0) + (26.0 * 60.0) + 21.448 ! epsilon0 is now in seconds
    a = a - (4680.93 * U)
    a = a - (1.55 * (U ** 2))
    a = a + (1999.25 * (U ** 3))
    a = a - (51.38 * (U ** 4))
    a = a - (249.67 * (U ** 5))
    a = a - (39.05 * (U ** 6))
    a = a + (7.12 * (U ** 7))
    a = a + (27.87 * (U ** 8))
    a = a + (5.79 * (U ** 9))
    a = a + (2.45 * (U ** 10))
    a = a / 3600.0 ! convert a from arcseconds to degrees

    !epsilon0 = 23.0 + (26.0 / 60.0) + (21.448 / 3600.0) - ((46.8450 * T) / 3600.0) - ((0.00059 * T * T) / 3600.0) + ((0.001813 * T * T * T) / 3600.0)
    epsilon0 = 23.0 + (26.0 / 60.0) + (21.448 / 3600.0) + a + delta_epsilon ! true obliquity of the ecliptic

    !epsilon0 = epsilon0 + delta_epsilon
    !epsilon0 = mod(epsilon0, 26.0) ! if the obliquity of the ecliptic is calculated more than 10,000 years from J2000.0. the numbers become silly. This keeps it within sensible boundaries.
    ! nut = (epsilon0, delta_psi)
    nut(0) = epsilon0
    nut(1) = delta_psi
    nut(2) = delta_epsilon
  end subroutine nutation
end module stellar_coords

module solar_coords
  use stellar_coords  
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
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, intent(out) :: tau

    tau = (jday - 2451545.0) / 365250

  end subroutine solar_tau

  subroutine solar_longitude(jday, longitude)
    ! Ecliptic longitude of Earth
    double precision, intent(in) :: jday
    double precision, intent(out) :: longitude

    ! Value for each term is given by A cos (B + C*tau)
    double precision :: L
    double precision :: L0
    double precision :: L1
    double precision :: L2
    double precision :: L3
    double precision :: L4
    double precision :: L5

    double precision, dimension(64,3) :: L0terms
    double precision, dimension(34,3) :: L1terms
    double precision, dimension(20,3) :: L2terms
    double precision, dimension( 7,3) :: L3terms
    double precision, dimension( 3,3) :: L4terms

    double precision :: tau
    integer :: i
    double precision :: k
    double precision :: pi
    double precision :: pi2

    pi = 4.0 * atan(1.0)
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
    L = L * (180.0 / pi)
    L = mod(L, 360.0)
    do while (L < 0.0)
       L = L + 360
    end do

    longitude = L + 180
    longitude = mod(longitude, 360.0)
    !print *, "longitude = ", longitude

  end subroutine solar_longitude

  subroutine solar_time(jday, angle, time)
    ! Get the time of that the sun hits angle, in minutes since midnight UTC.
    ! This can be off by up to 15 minutes in either direction because we live in a chaotic universe.
    ! There does not appear to be any more accurate algorithm that is readily available.
    double precision, intent(in) :: jday
    double precision, intent(in) :: angle
    double precision, intent(out) :: time

    double precision :: angle_today
    double precision :: angle_tomorrow
    double precision :: div

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
    
  subroutine solar_radec(jday, radec)
    ! Obtain the right ascension and declination of the sun
    ! Based on Meeus, chapter 13
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, dimension(2), intent(out) :: radec ! right ascension and declination

    double precision :: lon ! ecliptic longitude
    !double precision :: lat ! ecliptic latitude
    double precision, dimension(3) :: nut ! nutation factors

    double precision :: pi = 4.0 * atan(1.0)
    double precision :: d2r ! convert degrees to radians
    double precision :: r2d ! convert radians to degrees

    d2r = pi / 180.0
    r2d = 180.0 / pi

    call nutation(jday, nut)
    call solar_longitude(jday, lon) ! get ecliptic longitude                                                  

    ! compute the right ascension.
    ! Because the sun's ecliptic latitude is always 0 by definition, Meeus' equation simplifies to this in the case of the sun
    
    radec(1) = datand(dcosd(nut(1)) * dtand(lon))

    !print *, lon
    !print *, radec(1)
    ! Trig functions only really work between (-90)º and +90º;
    ! this next bit accounts for that, converting radec(1) to the correct value between 0º and 360º
    !if ((lon <= 90) .and. (radec(1) < 0)) then ! lambda in ALL quadrant, alpha in SIN quadrant
     !  radec(1) = 180 + radec(1)
    !else if ((lon <= 180) .and. (radec(1) < 0)) then ! lambda in SIN quadrant, alpha in SIN quadrant
     !  radec(1) = 180 + radec(1)
    !else if ((lon <= 180) .and. (radec(1) > 0)) then ! lambda in SIN quadrant, alpha in TAN quadrant
     !  radec(1) = 180 + radec(1)
     !else if ((lon <= 270) .and. (radec(1) > 0)) then ! lambda in TAN quadrant, alpha in TAN quadrant
      ! radec(1) = 180 + radec(1)
    !else if ((lon <= 270) .and. (radec(1) < 0)) then ! lambda in TAN quadrant, alpha in COS quadrant
    !  radec(1) = 360 + radec(1)
    !else if ((lon > 270) .and. (radec(1) < 0)) then ! lambda in COS quadrant, alpha in COS quadrant
     !  radec(1) = 360 + radec(1)
    !else if ((lon > 270) .and. (radec(1) >= 0)) then ! lambda in COS quadrant, alpha in ALL quadrant
     !  radec(1) = 0 + radec(1)
    !else if ((lon <= 90) .and. (radec(1) > 0)) then ! lambda in ALL quadrant, alpha in ALL quadrant
     !  radec(1) = 0 + radec(1)
    !end if

    if (lon <= 90.0) then ! lambda in ALL quadrant
       if (radec(1) >= 0.0) then ! alpha in ALL quadrant
          radec(1) = 0.0 + radec(1)
       else if (radec(1) < 0.0) then ! alpha in SIN quadrant
          radec(1) = 180.0 + radec(1)
     end if
  else if (lon <= 180.0) then ! lambda in SIN quadrant
     if (radec(1) < 0.0) then !alpha in SIN quadrant
        radec(1) = 180.0 + radec(1)
     else if (radec(1) >= 0.0) then ! alpha in TAN quadrant
        radec(1) = 180.0 + radec(1)
     end if
  else if (lon <= 270.0) then ! lambda in TAN quadrant
     if (radec(1) >= 0.0) then ! alpha in TAN quadrant
        radec(1) = 180.0 + radec(1)
     else if (radec(1) < 0.0) then ! alpha in COS quadrant
        radec(1) = 360.0 + radec(1)
     end if
  else if (lon <= 360.0) then ! lambda in COS quadrant
     if (radec(1) < 0.0) then ! alpha in COS quadrant
        radec(1) = 360.0 + radec(1)
     else if (radec(1) >= 0.0) then !alpha in ALL quadrant
        radec(1) = 0.0 + radec(1)
     end if
  end if
  radec(1) = modulo(radec(1), 360.0)
  
    ! compute the declination
    ! Again, because the sun's ecliptic latitude is always 0, the standard equation reduced to this
    radec(2) = asind(sind(nut(1)) * sind(lon))
    !radec(2) = modulo(radec(2), 360.0)
  end subroutine solar_radec
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
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, intent(out) :: T
    
    T = (jday - 2451545.0) / 36525.0
    
  end subroutine getT
  
  subroutine getD(T, D)
    ! Mean elonation of the moon
    double precision, intent(in) :: T
    double precision :: v
    double precision :: w
    double precision :: x
    double precision :: y
    double precision :: z
    double precision, intent(out) :: D
    
    v = 297.8501921
    w = 445267.1114034 * T
    x = 0.0018819 * (T ** 2)
    y = (T ** 3) / 545868.0
    z = (T ** 4) / 113065000.0
    
    D = v + w - x + y - z
    
    
  end subroutine getD
  
  subroutine getecc(T, ecc)
    ! Eccentricity of Earth's orbit
    double precision, intent(in) :: T ! Obtained a different module
    double precision :: a
    double precision :: b
    double precision, intent(out) :: ecc
    
    a = 0.002516 * T
    b = 0.0000074 * (T ** 2)
    
    ecc = 1 - a - b    
    
  end subroutine getecc
  
  subroutine getF(T, F)
    ! Moon's argument of latitude
    double precision, intent(in) :: T ! Obtained a different module
    double precision :: v
    double precision :: w
    double precision :: x
    double precision :: y
    double precision :: z
    double precision, intent(out) :: F
    
    v = 93.2720950
    w = 483202.0175233 * T
    x = 0.0036539 * (T ** 2)
    y = (T ** 3) / 3526000.0
    z = (T ** 4) / 863310000.0
    
    F = v + w - x - y + z    
    
  end subroutine getF
  
  subroutine getLprime(T, Lprime)
    ! Mean longitude of the moon (AKA mean equinox of date)
    double precision, intent(in) :: T ! Obtained a different module
    double precision :: v
    double precision :: w
    double precision :: x
    double precision :: y
    double precision :: z
    double precision, intent(out) :: Lprime
    
    v = 218.3164477
    w = 481267.88123421 * T
    x = 0.0015786 * (T ** 2)
    y = (T ** 3) / 538841.0
    z = (T ** 4) / 65194000.0
    
    Lprime = v + w - x + y - z
    
    
  end subroutine getLprime
  
  subroutine getM(T, M)
    ! Mean anomaly of the sun
    double precision, intent(in) :: T ! Obtainem a mifferent momule
    double precision :: v
    double precision :: w
    double precision :: x
    double precision :: y
    !double precision :: z
    double precision, intent(out) :: M
    
    v = 357.5291092
    w = 35999.0502909 * T
    x = 0.0001536 * (T ** 2)
    y = (T ** 3) / 24490000.0
    
    M = v + w - x + y
    
    
  end subroutine getM
  
  subroutine getMprime(T, Mprime)
    ! Mean anomaly of the moon
    double precision, intent(in) :: T ! Obtained a different module
    double precision :: v
    double precision :: w
    double precision :: x
    double precision :: y
    double precision :: z
    double precision, intent(out) :: Mprime
    
    v = 134.9633964
    w = 477198.8675055 * T
    x = 0.0087414 * (T ** 2)
    y = (T ** 3) / 69699.0
    z = (T ** 4) / 14712000.0
    
    Mprime = v + w - x + y - z
    
    
  end subroutine getMprime
  
  subroutine lunar_lonlat(jre, lonlat)
    double precision, intent(in) :: jre
    double precision, dimension(2), intent(out) :: lonlat
    double precision :: T
    double precision :: Lprime
    double precision :: D
    double precision :: M
    double precision :: Mprime
    double precision :: F
    double precision :: ecc ! solar eccentricity
    double precision :: a1
    double precision :: a2
    double precision :: a3
    integer, dimension(60,6) :: ltable
    integer, dimension(60,5) :: btable
    !double precision :: Dterm
    !double precision :: Mterm
    !double precision :: Mpterm
    !double precision :: Fterm
    !double precision :: term
    double precision :: sigma_l ! used to calculate lunar longitude
    double precision :: sigma_b ! used to calculate lunar latitude
    integer :: i
    double precision :: pi = 4.0 * atan(1.0)
    double precision :: d2r ! convert degrees to radians
    double precision :: r2d ! convert radians to degrees

    d2r = 180.0 / pi
    r2d = pi / 180.0

    ltable(1,:) =  [0,  0,  1,  0, 6288774, -20905355]
    ltable(2,:) =  [2,  0, -1,  0, 1274027,  -3699111]
    ltable(3,:) =  [2,  0,  0,  0,  658314,  -2955968]
    ltable(4,:) =  [0,  0,  2,  0,  213618,   -569925]
    ltable(5,:) =  [0,  1,  0,  0, -185116,     48888]
    ltable(6,:) =  [0,  0,  0,  2, -114332,     -3149]
    ltable(7,:) =  [2,  0, -2,  0,   58793,    246158]
    ltable(8,:) =  [2, -1, -1,  0,   57066,   -152138]
    ltable(9,:) =  [2,  0,  1,  0,   53322,   -170733]
    ltable(10,:) = [2, -1,  0,  0,   45758,   -204586]
    ltable(11,:) = [0,  1, -1,  0,  -40923,   -129620]
    ltable(12,:) = [1,  0,  0,  0,  -34720,    108743]
    ltable(13,:) = [0,  1,  1,  0,  -30383,    104755]
    ltable(14,:) = [2,  0,  0, -2,   15327,     10321]
    ltable(15,:) = [0,  0,  1,  2,  -12528,         0]
    ltable(16,:) = [0,  0,  1, -2,   10980,     79661]
    ltable(17,:) = [4,  0, -1,  0,   10675,    -34782]
    ltable(18,:) = [0,  0,  3,  0,   10034,    -23210]
    ltable(19,:) = [4,  0, -2,  0,    8548,    -21636]
    ltable(20,:) = [2,  1, -1,  0,   -7888,     24208]
    ltable(21,:) = [2,  1,  0,  0,   -6766,     30824]
    ltable(22,:) = [1,  0, -1,  0,   -5163,     -8379]
    ltable(23,:) = [1,  1,  0,  0,    4987,    -16675]
    ltable(24,:) = [2, -1,  1,  0,    4036,    -12831]
    ltable(25,:) = [2,  0,  2,  0,    3994,    -10445]
    ltable(26,:) = [4,  0,  0,  0,    3861,    -11650]
    ltable(27,:) = [2,  0, -3,  0,    3665,     14403]
    ltable(28,:) = [0,  1, -2,  0,   -2689,     -7003]
    ltable(29,:) = [2,  0, -1,  2,   -2602,         0]
    ltable(30,:) = [2, -1, -2,  0,    2390,     10056]
    ltable(31,:) = [1,  0,  1,  0,   -2348,      6322]
    ltable(32,:) = [2, -2,  0,  0,    2236,     -9884]
    ltable(33,:) = [0,  1,  2,  0,   -2120,      5751]
    ltable(34,:) = [0,  2,  0,  0,   -2069,         0]
    ltable(35,:) = [2, -2, -1,  0,    2048,     -4950]
    ltable(36,:) = [2,  0,  1, -2,   -1773,      4130]
    ltable(37,:) = [2,  0,  0,  2,   -1595,         0]
    ltable(38,:) = [4, -1, -1,  0,    1215,     -3958]
    ltable(39,:) = [0,  0,  2,  2,   -1110,         0]
    ltable(40,:) = [3,  0, -1,  0,    -892,      3258]
    ltable(41,:) = [2,  1,  1,  0,    -810,      2616]
    ltable(42,:) = [4, -1, -2,  0,     759,     -1897]
    ltable(43,:) = [0,  2, -1,  0,    -713,     -2117]
    ltable(44,:) = [2,  2, -1,  0,    -700,      2354]
    ltable(45,:) = [2,  1, -2,  0,     691,         0]
    ltable(46,:) = [2, -1,  0, -2,     596,         0]
    ltable(47,:) = [4,  0,  1,  0,     549,     -1423]
    ltable(48,:) = [0,  0,  4,  0,     537,     -1117]
    ltable(49,:) = [4, -1,  0,  0,     520,     -1571]
    ltable(50,:) = [1,  0, -2,  0,    -487,     -1739]
    ltable(51,:) = [2,  1,  0, -2,    -399,         0]
    ltable(52,:) = [0,  0,  2, -2,    -381,     -4421]
    ltable(53,:) = [1,  1,  1,  0,     351,         0]
    ltable(54,:) = [3,  0, -2,  0,    -340,         0]
    ltable(55,:) = [4,  0, -3,  0,     330,         0]
    ltable(56,:) = [2, -1,  2,  0,     327,         0]
    ltable(57,:) = [0,  2,  1,  0,    -323,      1165]
    ltable(58,:) = [1,  1, -1,  0,     299,         0]
    ltable(59,:) = [2,  0,  3,  0,     294,         0]
    ltable(60,:) = [2,  0, -1, -2,       0,      8752]

    btable( 1,:) = [0,  0,  0,  1, 5128122]
    btable( 2,:) = [0,  0,  1,  1,  280602]
    btable( 3,:) = [0,  0,  1, -1,  277693]
    btable( 4,:) = [2,  0,  2, -1,  173237]
    btable( 5,:) = [2,  0, -1,  1,   55413]
    btable( 6,:) = [2,  0, -1, -1,   46271]
    btable( 7,:) = [2,  0,  0,  0,   32573]
    btable( 8,:) = [0,  0,  2,  1,   17198]
    btable( 9,:) = [2,  0,  1, -1,    9266]
    btable(10,:) = [0,  0,  2, -1,    8822]
    btable(11,:) = [2, -1,  0, -1,    8216]
    btable(12,:) = [2,  0, -2, -1,    4324]
    btable(13,:) = [2,  0,  1,  1,    4200]
    btable(14,:) = [2,  1,  0, -1,   -3359]
    btable(15,:) = [2, -1, -1,  1,    2463]
    btable(16,:) = [2, -1,  0,  1,    2211]
    btable(17,:) = [2, -1, -1, -1,    2065]
    btable(18,:) = [0,  1, -1, -1,   -1870]
    btable(19,:) = [4,  0, -1, -1,    1828]
    btable(20,:) = [0,  1,  0,  1,   -1794]
    btable(21,:) = [0,  0,  0,  3,   -1749]
    btable(22,:) = [0,  1, -1,  1,   -1565]
    btable(23,:) = [1,  0,  0,  0,   -1491]
    btable(24,:) = [0,  1,  1,  1,   -1475]
    btable(25,:) = [0,  1,  1, -1,   -1410]
    btable(26,:) = [0,  1,  0, -1,   -1344]
    btable(27,:) = [1,  0,  0, -1,   -1335]
    btable(28,:) = [0,  0,  3,  1,    1107]
    btable(29,:) = [4,  0,  0, -1,    1021]
    btable(30,:) = [4,  0, -1,  1,     833]
    btable(31,:) = [0,  0,  1, -3,     777]
    btable(32,:) = [4,  0, -2,  1,     671]
    btable(33,:) = [2,  0,  0, -3,     607]
    btable(34,:) = [2,  0,  2, -1,     596]
    btable(35,:) = [2, -1,  1, -1,     491]
    btable(36,:) = [2,  0, -2,  1,    -451]
    btable(37,:) = [0,  0,  3, -1,     439]
    btable(38,:) = [2,  0,  2,  1,     422]
    btable(39,:) = [2,  0, -3, -1,     421]
    btable(40,:) = [2,  1, -1,  1,    -366]
    btable(41,:) = [2,  1,  0,  1,    -351]
    btable(42,:) = [4,  0,  0,  1,     331]
    btable(43,:) = [2, -1,  1,  1,     315]
    btable(44,:) = [2, -2,  0, -1,     302]
    btable(45,:) = [0,  0,  1,  3,    -283]
    btable(46,:) = [2,  1,  1, -1,    -229]
    btable(47,:) = [1,  1,  0, -1,     223]
    btable(48,:) = [1,  1,  0,  1,     223]
    btable(49,:) = [0,  1, -2, -1,    -220]
    btable(50,:) = [2,  1, -1, -1,    -220]
    btable(51,:) = [1,  0,  1,  1,    -185]
    btable(52,:) = [2, -1, -2, -1,     181]
    btable(53,:) = [0,  1,  2,  1,    -177]
    btable(54,:) = [4,  0, -2, -1,     176]
    btable(55,:) = [4, -1, -1, -1,     166]
    btable(56,:) = [1,  0,  1, -1,    -164]
    btable(57,:) = [4,  0,  1, -1,     132]
    btable(58,:) = [1,  0, -1, -1,    -119]
    btable(59,:) = [4, -1,  0,  1,     115]
    btable(60,:) = [2, -2,  0,  1,     107]    

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

    sigma_l = 0.0
    sigma_b = 0.0

    do i = 1, 60
       sigma_l = sigma_l + (ltable(i,5) * (ecc ** abs(ltable(i,2))) * dsind( (D * ltable(i,1)) + (M * ltable(i,2)) + (Mprime * ltable(i,3)) + (F * ltable(i,4)) )) ! lunar longitude
       sigma_b = sigma_b + (btable(i,5) * (ecc ** abs(btable(i,2))) * dsind( (D * btable(i,1)) + (M * btable(i,2)) + (Mprime * btable(i,3)) + (F * btable(i,4)) )) ! lunar latitude
       !sigma_l = sigma_l + (ltable(i,5) * (ecc ** abs(ltable(i,2))) * sin( d2r * (D * ltable(i,1)) + (M * ltable(i,2)) + (Mprime * ltable(i,3)) + (F * ltable(i,4)) )) ! lunar longitude
       !sigma_b = sigma_b + (btable(i,5) * (ecc ** abs(btable(i,2))) * sin(d2r * (D * btable(i,1)) + (M * btable(i,2)) + (Mprime * btable(i,3)) + (F * btable(i,4)) )) ! lunar latitude       

       !Dterm = D * ltable(i, 1)
       !Mterm = M * ltable(i, 2)
       !Mpterm = Mprime * ltable(i, 3)
       !Fterm = F * ltable(i, 4)
       !term = ltable(i, 5) * (ecc ** abs(ltable(i, 2))) * sind(Dterm + Mterm + Mpterm + Fterm)
       
       !sigma_l = sigma_l + term
    end do

    sigma_l = sigma_l + (3958 * dsind(a1)) + (1962 * dsind(Lprime - F)) + (318 * dsind(a2))
    sigma_b = sigma_b - (2235 * dsind(Lprime)) + (382 * dsind(a3)) + (175 * dsind(a1 - F)) + (175 * dsind(a1 +F)) + (127 * dsind(Lprime - Mprime)) - (115 * dsind(Lprime + Mprime))

    lonlat(1) = Lprime + (sigma_l / 1000000.0) ! lunar longitude
    lonlat(2) = sigma_b / 1000000.0 ! lunar latitude
    lonlat(1) = modulo(lonlat(1), 360.0)

    !lambda = Lprime + (sigma_l / 1000000)
    !lambda = lambda + 0.004610    
    !lambda = mod(lambda, 360.0)
    !do while (lambda < 0.0)
     !  lambda = lambda + 360.0
    !end do
    !lambda = double precision(lambda)

  end subroutine lunar_lonlat

  subroutine lunar_longitude(jday, lon)
    ! get the ecliptic longitude of the moon as of jday
    double precision, intent(in)  :: jday
    double precision, intent(out) :: lon ! ecliptic longitude

    double precision, dimension(2) :: lonlat

    call lunar_lonlat(jday, lonlat)
    lon = lonlat(1)

  end subroutine lunar_longitude

  subroutine lunar_latitude(jday, lat)
    ! get the ecliptic latitude of the moon as of jday
    double precision, intent(in)  :: jday
    double precision, intent(out) :: lat ! ecliptic latitude

    double precision, dimension(2) :: lonlat

    call lunar_lonlat(jday, lonlat)
    lat = lonlat(2)

  end subroutine lunar_latitude

  subroutine lunar_time(jday, time)
    ! Find the minute of the new moon
    double precision, intent(in) :: jday
    integer, intent(out) :: time ! in minutes

    double precision :: moon_today ! ecliptic longitude of the moon at midnight
    double precision :: moon_tomorrow ! ecliptic longitude of the moon at midnight tomorrow
    double precision :: sun_today ! ecliptic longitude of the sun at midnight
    double precision :: sun_tomorrow ! ecliptic longitude of the sun at midnight tomorrow
    double precision :: lunar_div
    double precision :: solar_div
    integer :: minutes
    double precision :: day

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

  subroutine lunar_radec(jday, radec)
    ! obtain the right ascension and declination of the moon
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, dimension(2), intent(out) :: radec ! moon's right ascension and declination

    double precision, dimension(3) :: nut ! nutation factors
    double precision, dimension(2) :: lonlat ! lunar longitude and latitude

    double precision :: pi = 4.0 * atan(1.0)
    double precision :: d2r ! convert degrees to radians
    double precision :: r2d ! convert radians to degrees

    d2r = pi / 180.0
    r2d = 180.0 / pi

    call nutation(jday, nut)
    call lunar_lonlat(jday, lonlat)
    !call lunar_longitude(jday, lon)
    !call lunar_latitude(jday, lat)

    radec(1) = datand(((dsind(lonlat(1)) * dcosd(nut(1))) - (dtand(lonlat(2)) * dsind(nut(1)))) / dcosd(lonlat(1))) ! right ascension
    radec(2) = dasind((dsind(lonlat(2)) * dcosd(nut(1))) + (dcosd(lonlat(2)) * dsind(nut(1)) * dsind(lonlat(1)))) ! declination

    ! as with the solar celestial coordinates, things get a bit wonky when the angles aren't between -90 and +90
    ! hence this block
    if (lonlat(1) <= 90.0) then ! lambda in ALL quadrant
       if (radec(1) >= 0.0) then ! alpha in ALL quadrant
          radec(1) = 0.0 + radec(1)
       else if (radec(1) < 0.0) then ! alpha in SIN quadrant
          radec(1) = 180.0 + radec(1)
       end if
    else if (lonlat(1) <= 180.0) then ! lambda in SIN quadrant
       if (radec(1) < 0.0) then !alpha in SIN quadrant
          radec(1) = 180.0 + radec(1)
       else if (radec(1) >= 0.0) then ! alpha in TAN quadrant
          radec(1) = 180.0 + radec(1)
       end if
    else if (lonlat(1) <= 270.0) then ! lambda in TAN quadrant
       if (radec(1) >= 0.0) then ! alpha in TAN quadrant
          radec(1) = 180.0 + radec(1)
       else if (radec(1) < 0.0) then ! alpha in COS quadrant
          radec(1) = 360.0 + radec(1)
       end if
    else if (lonlat(1) <= 360.0) then ! lambda in COS quadrant
       if (radec(1) < 0.0) then ! alpha in COS quadrant
          radec(1) = 360.0 + radec(1)
       else if (radec(1) >= 0.0) then !alpha in ALL quadrant
          radec(1) = 0.0 + radec(1)
       end if
    end if

    radec(1) = modulo(radec(1), 360.0)
    !radec(2) = modulo(radec(2), 360.0)
  end subroutine lunar_radec
  
  
end module lunar_coords


module sidereal
  ! Sidereal calculations, including times of rising and setting
  use stellar_coords
  use solar_coords
  implicit none

contains

  subroutine precession(jday, ra2000, dec2000, distance, rv, deltara, deltadec, answer)
    ! apply the effect of precession to obtain
    ! the actual right ascension and declination

    double precision, intent(in) :: jday ! Julian Day in question
    double precision, intent(in) :: ra2000 ! right ascension at J2000.0, in DEGREES
    double precision, intent(in) :: dec2000 ! declination at J2000.0, in DEGREES
    double precision, intent(in) :: distance ! distance from the sun, in PARSECS
    double precision, intent(in) :: rv ! radial velocity, in parsecs per year
    double precision, intent(in) :: deltara ! right ascension component of proper motion, in ARCSECONDS. This has to be looked up
    double precision, intent(in) :: deltadec ! declination component of proper motion,m in ARCSECONDS. This has to be looked up.
    !integer, intent(in) :: id ! sun or a star?
    double precision, dimension(2), intent(out) :: answer ! RA and Dec for use in calculations

    double precision :: pi
    double precision :: d2r ! convert degrees to radians
    double precision :: r2d ! convert radians to degrees

    double precision :: t ! Julian centuries since J2000.0
    double precision :: zeta
    double precision :: z
    double precision :: theta

    double precision :: a ! placeholder
    double precision :: b ! placeholder
    double precision :: c ! placeholder

    double precision, dimension(2) :: radec ! RA and Dec after accounting for proper motion but before accounting for precession
    double precision :: ra ! right ascension after taking proper motion into account
    double precision :: dec ! declination after taking proper motion into account

    !double precision, dimension(2) :: nut ! nutation numbers

    pi = 4.0 * atan(1.0)
    d2r = pi / 180.0
    r2d = 180.0 / pi

    !print *, jday, ra2000, dec2000, distance, rv, deltara, deltadec
    !if (distance /= 0) then
       !call propmot(jday, ra2000, dec2000, distance, rv, deltara, deltadec, radec)
    !end if
    !print *, "Before: ", ra2000, dec2000
    
    call propmot(jday, ra2000, dec2000, distance, rv, deltara, deltadec, radec)
    ra = radec(1)
    dec = radec(2)
    t = (jday - 2451545.0) / 36525.0
    !print *, "radec: ", radec
    
    zeta = (2306.2181 * t) + (0.30188 * t * t) + (0.017998 * (t ** 3))
    z = (2306.2181 * t) + (1.09468 * t * t) + (0.018203 * (t ** 3))
    theta = (2004.3109 * t) + (0.42665 * t * t) + (0.041833 * (t ** 3))
    !print *, zeta
    !print *, z
    !print *, theta
    
    ! zeta, z, and theta are in ARCSECONDS, and so need to be converted into radians for the next bit
    
    a = cos(d2r * dec) * sin(d2r * (ra + (zeta / 3600.0)))    
    b = cos(d2r * (theta / 3600.0))
    b = b * cos(d2r * dec)
    b = b * cos(d2r * (ra + (zeta / 3600.0)))
    b = b - (sin(d2r * (theta / 3600.0)) * sin(d2r * dec))
    c = sin(d2r * (theta / 3600.0))
    c = c * cos(d2r * dec)
    c = c * cos(d2r * (ra + (zeta / 3600.0)))
    c = c + (cos(d2r * (theta / 3600.0)) * sin(d2r * dec))
    
    !print *, a, b, c
    !print *, a/b
    !print *, atan(a/b)
    
    !answer(1) = z + (r2d * atan(a / b)) ! right ascension, in degrees, taking both proper motion and precession into accont
    answer(1) = atan(a/b)
    if ((a/b) >= 0) then
       if ((ra2000 <= 135.0) .or. (ra2000 >= 315.0)) then ! ra in ALL quadrant
          answer(1) = 0 + answer(1)
       else ! ra in TAN quadrant
          answer(1) = pi + answer(1)
       end if
    else if ((a/b) < 0) then
       if ((ra2000 >= 45.0) .and. (ra2000 <= 235.0)) then ! ra in SIN quadrant
          answer(1) = pi + answer(1)
       else ! ra in COS quadrant
          answer(1) = (2 * pi) + answer(1)
       end if
    end if
    
    answer(1) = (z / 3600.0) + (r2d * answer(1))
    !print *, answer(1)
    !print *, z
    
    answer(2) = r2d * asin(c) ! declination, in degrees, taking both proper motion and precession into account
    
    !ra = radec(1)
    !dec = radec(2)
    !print *, radec
    !print *, ra
    !print *, dec
    !print *, "After: ", answer
  end subroutine precession

  subroutine getsid(jday, midnight)
    ! Calculate sidereal time at Greenwich
    ! Based on Meeus, chapter 12
    double precision, intent(in) :: jday ! Julian Day in question; must end in 0.5 because we're interested in midnight
    !double precision, intent(in) :: inst ! time since midnight that we're interested in
    !double precision, intent(out), dimension(2) :: sid ! Sidereal time at midnight and at the desired moment
    double precision, intent(out) :: midnight

    double precision :: T ! Julian centuries since J2000.0
    ! double precision :: midnight ! Sidereal time at midnight
    ! double precision :: alpha
    double precision :: corr ! correction to mean sidereal time to get apparent sidereal time
    double precision, dimension(3) :: epsi ! nutation factors
    double precision :: d2r ! convert degrees to radians

    T = (jday - 2451545.0) / 36525.0
    midnight = 100.46061837 + (36000.770053608 * T) + (0.000387933 * T * T) - ((T ** 3) / 38710000.0)
    !alpha = inst * 1.00273790935
    !theta = midnight + alpha

    d2r = 4.0 * atan(1.0) / 180.0
    call nutation(jday, epsi)
    corr = (epsi(2) * cos(d2r * epsi(1))) / 15.0
    midnight = midnight + corr
    !theta = theta + corr
    !sid = (midnight, theta)
  end subroutine getsid

  subroutine sidstant(jday, inst, answer)
    ! Calculate sidereal time for any instant at Greenwich
    ! Based on Meeus, chapter 12
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, intent(in) :: inst ! time since midnight that we're interested in
    double precision, intent(out) :: answer ! sidereal time at inst

    double precision :: midnight ! sidereal time at midnight
    double precision :: inc ! amount to add to the time at midnight

    call getsid(jday, midnight)
    inc = inst * 1.00273790935
    answer = midnight + inc
  end subroutine sidstant

  subroutine solar_riset(jday, lon, lat, time)
    ! Calculte the time of sunrise and sunset
    ! Based on Meeus, chapter 15
    
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, intent(in) :: lon ! observer's longitude, in degrees
    double precision, intent(in) :: lat ! observer's latitude, in degrees
    !double precision, intent(in) :: deltat
    double precision, dimension(2), intent(out) :: time ! time of sunrise and sunset, in days and fractions of a day

    double precision :: ra2000
    double precision :: dec2000 
    double precision :: pi
    double precision :: d2r ! convert degrees to radians
    double precision :: r2d ! convert radians to degrees

    double precision :: h0 ! standard altitude, in degrees    
    double precision :: testval ! initial check
    ! double precision :: approx ! approximate time related to sunset

    double precision :: sid ! Sidereal time at midnight on the day in question
    double precision :: bigh
    
    double precision :: transit ! time the sun crosses the meridian
    !double precision :: theta_r ! sidereal time of the sunrise converted into degrees
    !double precision :: theta_s ! sidereal time of the sunset converted into degrees

    !double precision :: delta_r ! modification to get true rising time
    !double precision :: delta_s ! modification to get true setting time

    double precision, dimension(2) :: yesterday ! RA and dec of prev day
    double precision, dimension(2) :: today ! RA and dec of day
    double precision, dimension(2) :: tomorrow ! RA and dec of next day
    !integer :: id ! sun or star!
    double precision, dimension(3) :: nut ! nutation values for use in calculating the sun's position
    
    pi = 4.0 * atan(1.0)
    d2r = pi / 180.0
    r2d = 180.0 / pi

    ra2000 = 281.29
    dec2000 = 0 - (23 + (2.0/60.0) + (8.2/3600.0))

    h0 = -0.8333 ! this is in degrees, not radians
    call nutation(jday, nut)
    call solar_radec(jday - 1, yesterday)
    call solar_radec(jday, today)
    call solar_radec(jday + 1, tomorrow)

    testval = (sin(d2r * h0) - (sin(d2r * lat) * sin(d2r * today(2)))) / (cos(d2r * lat) * cos(d2r * today(2)))
    if (abs(testval) > 1.0) then
       time = 25.0
    else
       bigh = acos(testval)
       !print *, testval
       !print *, (r2d * bigh)
       call getsid(jday, sid)
       !sid = mod(sid, 360.0)
       !print *, "sid = ", sid
       !print *, (bigh / 360.0)
       
       transit = (today(1) + lon - sid) / 360.0
       !print *, "transit = ", transit
       time(1) = transit - ((r2d * bigh) / 360.0) ! sunrise
       time(2) = transit + ((r2d * bigh) / 360.0) ! sunset

       do while (time(1) < 0)
          time(1) = time(1) + 1.0
       end do
       do while (time(2) < 0)
          time(2) = time(2) + 1.0
       end do

       time(1) = mod(time(1), 1.0)
       time(2) = mod(time(2), 1.0)
    end if
  end subroutine solar_riset


  subroutine stellar_riset(jday, lon, lat, deltat, ra2000, dec2000, distance, rv, deltara, deltadec, time)
    ! Calculate time of rising and setting
    ! Based on Meeus, chapter 15

    ! This ignores the effect of atmospheric refraction because it's very very very small and too unpredicatable.
    
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, intent(in) :: lon ! observer's longitude, in degrees
    double precision, intent(in) :: lat ! observer's latitude, in degrees
    double precision, intent(in) :: deltat ! difference between universal time and dynamical time
    !double precision, dimension(2), intent(in) :: yesterday ! RA and Dec for the previous day. This algorithm assumes they are in radians
    !double precision, dimension(2), intent(in) :: today ! RA and Dec for day in question. This algorithm assumes they are in radians
    !double precision, dimension(2), intent(in) :: tomorrow ! RA and Dec for next day. This algorithm assumes they are in radians
    double precision, intent(in) :: ra2000 ! right ascension at J2000.0, in degrees. This has to be looked up.
    double precision, intent(in) :: dec2000 ! declination at J2000.0, in degrees. This has to be looked up.
    double precision, intent(in) :: distance ! distance from the sun, in parsecs. This has to be looked up.
    double precision, intent(in) :: rv ! radial velocity, in parsecs per year
    double precision, intent(in) :: deltara ! RA component of proper motion, in ARCSECONDS. This has to be looked up.
    double precision, intent(in) :: deltadec ! Dec component of proper motion, in ARCSECONDS. This has to be looked up.
!    integer, intent(in) :: id !What is actually rising or setting?
    double precision, dimension(2), intent(out) :: time ! time of sunrise and sunset, in days and fractions of a day
    
    double precision :: pi
    double precision :: d2r ! convert degrees to radians
    double precision :: r2d ! convert radians to degrees

    double precision :: h0 ! standard altitude, in degrees    
    double precision :: testval ! initial check
    ! double precision :: approx ! approximate time related to sunset

    double precision :: sid ! Sidereal time at midnight on the day in question
    double precision :: bigh
    
    !double precision :: nr ! used in calculating a modification to the rise time
    !double precision :: ns ! used in calculating a modification to the set time
    !double precision :: a_ra ! used in calculating interpolation
    !double precision :: b_ra ! used in calculating interpolation
    !double precision :: c_ra  ! used in calculating interpolation
    !double precision :: a_dec ! used in calculating interpolation
    !double precision :: b_dec ! used in calculating interpolation
    !double precision :: c_dec ! used in calculating interpolation
    !double precision :: rai_r ! right ascension, interpolated, for sunrise
    !double precision :: deci_r ! declination, interpolated, for sunrise
    !double precision :: rai_s ! right ascension, interpolated, for sunset
    !double precision :: deci_s ! declination, interpolated, for sunset
    ! double precision, dimension(2) :: inr ! interpolated RA and dec for sunrise
    ! double precision, dimension(2) :: ins ! interpolated RA and dec for sunset
    !double precision :: alt_r ! altitude at sunrise
    !double precision :: alt_s ! altitude at sunset
    !double precision :: ha_r ! hour angle of rising sun, in degrees
    !double precision :: ha_s ! hour angle of setting sun, in degrees
    
    double precision :: transit ! time the sun crosses the meridian
    !double precision :: theta_r ! sidereal time of the sunrise converted into degrees
    !double precision :: theta_s ! sidereal time of the sunset converted into degrees

    !double precision :: delta_r ! modification to get true rising time
    !double precision :: delta_s ! modification to get true setting time

    double precision, dimension(2) :: yesterday ! RA and dec of prev day
    double precision, dimension(2) :: today ! RA and dec of day
    double precision, dimension(2) :: tomorrow ! RA and dec of next day
    !integer :: id ! sun or star!
    double precision, dimension(2) :: nut ! nutation values for use in calculating the sun's position
    
    pi = 4.0 * atan(1.0)
    d2r = pi / 180.0
    r2d = 180.0 / pi

    h0 = -0.5667 ! this is in degrees, not radians

       !print *, h0
       !print *, jday
       !print *, ra2000
       !print *, dec2000
       !print *, distance
       !print *, rv
       !print *, deltara
       !print *, deltadec
    
    call precession((jday - 1), ra2000, dec2000, distance, rv, deltara, deltadec, yesterday) ! right ascension and declination of the previous day, in degrees
    call precession(jday, ra2000, dec2000, distance, rv, deltara, deltadec, today) ! right ascension and declination of the day in question, in degrees
    call precession((jday + 1), ra2000, dec2000, distance, rv, deltara, deltadec, tomorrow) ! right ascension and declination of the next day, in degrees

    !print *, "Initial values: ", ra2000, dec2000
    !print *, "Yesterday: ", yesterday
    !print *, "Today: ", today
    !print *, "Tomorrow: ", tomorrow
  
    testval = (sin(d2r * h0) - (sin(d2r * lat) * sin(d2r * today(2)))) / (cos(d2r * lat) * cos(d2r * today(2)))
    !print *, yesterday
    !print *, today
    !print *, tomorrow
    !print *, testval
    !print *, yesterday
    !print *, today
    !print *, tomorrow
    !print *, sin(d2r * h0)
    !print *, sin(d2r * lat)
    !print *, sin(d2r * tomorrow(2))
    !print *, (sin(d2r * h0) - (sin(d2r * lat) * sin(d2r * tomorrow(2))))
    !print *, cos(d2r * lat)
    !print *, cos(d2r * tomorrow(2))
    !print *, cos(d2r * lat) * cos(d2r * tomorrow(2))
    !print *, testval
    if (abs(testval) > 1.0) then
       time = 25.0
    else
       bigh = acos(testval)
       !print *, "bigh = ", (r2d * bigh)
       !print *, testval
       !print *, (r2d * bigh)
       call getsid(jday, sid)
       !sid = mod(sid, 360.0)
       !print *, "sid = ", sid
       !print *, (bigh / 360.0)
       
       transit = (today(1) + lon - sid) / 360.0
       !print *, "transit = ", transit
       time(1) = transit - ((r2d * bigh) / 360.0) ! sunrise
       time(2) = transit + ((r2d * bigh) / 360.0) ! sunset

       do while (time(1) < 0)
          time(1) = time(1) + 1.0
       end do
       do while (time(2) < 0)
          time(2) = time(2) + 1.0
       end do

       time(1) = mod(time(1), 1.0)
       time(2) = mod(time(2), 1.0)

       ! the rest of this stuff is supposed to give a more accurate result,
       ! but in my testing the results obtained at this point accord better with reality
       ! could be I'm making an error in the interpolation
       ! Either way, screw it. I'll leave this stuff here,
       ! but commented out until I figure out how to use it properly


       !theta_r = sid + (360.985647 * time(1))
       !theta_s = sid + (360.985647 * time(2))

       !nr = time(1) + (deltat / 86400.0)
       !ns = time(2) + (deltat / 86400.0)

       ! interpolation

       ! RA interpolation
       !a_ra = today(1) - yesterday(1)
       !b_ra = tomorrow(1) - today(1)
       !c_ra = b_ra - a_ra
       !rai_r = (nr / 2.0) * (a_ra + b_ra + (nr * c_ra))
       !rai_s = (ns / 2.0) * (a_ra + b_ra + (ns * c_ra))

       ! dec interpolation
       !a_dec = today(2) - yesterday(2)
       !b_dec = tomorrow(2) - today(2)
       !c_dec = b_dec - a_dec
       !deci_r = (nr / 2.0) * (a_dec + b_dec + (nr * c_dec))
       !deci_s = (ns / 2.0) * (a_dec + b_dec + (ns * c_dec))

       !ha_r = theta_r - lon - rai_r
       !ha_s = theta_s - lon - rai_s       

       !alt_r = r2d * asin((sin(d2r * lat) * sin(d2r * deci_r)) + (cos(d2r * lat) * cos(ha_r)))
       !alt_s = r2d * asin((sin(d2r * lat) * sin(d2r * deci_r)) + (cos(d2r * lat) * cos(ha_r)))

       ! MAKE SURE alt IS IN DEGREES. IF NOT, BE SURE TO CORRECT IT.

       !delta_r = (alt_r - h0) / (360.0 * cos(deci_r * d2r) * cos(lat * d2r) * sin(bigh))
       !delta_s = (alt_s - h0) / (360.0 * cos(deci_s * d2r) * cos(lat * d2r) * sin(bigh))
       !print *, delta_r
       !print *, delta_s

       !time(1) = time(1) + delta_r
       !time(2) = time(2) + delta_s

       ! time(x) now gives the fraction of a day that has elapsed since midnight when the body rises (x == 1) or sets (x == 2)
       ! these can be compared to floats, Fractions, and Decimals in Python, but might need to be converted into other units
       ! multiply time(x) by 24 to get the time in hours (which will still have a decimal portion; for example, 06:30 would register as 6.5)
       ! multiply time(x) by 1440 to get the time in minutes, or by 86400 to get the time in seconds.
       ! time(x) can even be multiplied by 25920 to get the time in chalakim.
    end if
    !print *, time
  end subroutine stellar_riset
end module sidereal

module pub
  ! subroutines which can be called from outside this library
  ! I'm doing this because, depending on your environment, it might not be possible to directly
  ! call a subroutine if its module is used by another module
  use stellar_coords
  use solar_coords
  use lunar_coords
  use sidereal
  implicit none

contains
  subroutine pub_solar_longitude(jday, lon)
    ! Returns solar longitude at a given time
    double precision, intent(in)  :: jday ! Julian Day in question
    double precision, intent(out) :: lon  ! solar longitude
    call solar_longitude(jday, lon)
  end subroutine pub_solar_longitude

  subroutine pub_lunar_longitude(jday, lon)
    ! Returns lunar longitude at a given time
    double precision, intent(in)  :: jday ! Julian Day in question
    double precision, intent(out) :: lon  ! lunar longitude
    call lunar_longitude(jday, lon)
  end subroutine pub_lunar_longitude

  subroutine pub_lunar_latitude(jday, lat)
    ! return lunar latitude at a given time
    double precision, intent(in)  :: jday ! Julian Day in question
    double precision, intent(out) :: lat  ! lunar latitude
    call lunar_latitude(jday, lat)
  end subroutine pub_lunar_latitude

  subroutine lunar_ecliptic_coords(jday, lonlat)
    ! returns lunar longitude and latitude at a given time
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, dimension(2), intent(out) :: lonlat
    call lunar_lonlat(jday, lonlat)
  end subroutine lunar_ecliptic_coords

  subroutine lunar_celestial_coords(jday, radec)
    ! returns lunar right ascension and declination at a given time
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, dimension(2), intent(out) :: radec
    call lunar_radec(jday, radec)
  end subroutine lunar_celestial_coords

  subroutine pub_solar_time(jday, angle, time)
    ! Returns the time that the sun hits a given ecliptic longitude
    double precision, intent(in)  :: jday  ! Julian Day in question
    double precision, intent(in)  :: angle ! ecliptic longitude
    double precision, intent(out) :: time  ! time that the sun hits angle
    call solar_time(jday, angle, time)
  end subroutine pub_solar_time

  subroutine pub_lunar_time(jday, time)
    ! Returns the time of the new moon closes to jday
    double precision, intent(in)  :: jday ! Julian Day we're starting with
    integer, intent(out) :: time ! Time of the new moon
    call lunar_time(jday, time)
  end subroutine pub_lunar_time

  subroutine pub_solar_riset(jday, lon, lat, time)
    ! Returns the time of sunrise and sunset on a given day
    double precision, intent(in)  :: jday ! Julian Day in question
    double precision, intent(in)  :: lon  ! Observer's geographical longitude, in degrees
    double precision, intent(in)  :: lat  ! Observer's geographical latitude, in degrees
    double precision, dimension(2), intent(out) :: time ! Time of sunrise and sunset
    call solar_riset(jday, lon, lat, time)
  end subroutine pub_solar_riset

  subroutine pub_stellar_riset(jday, lon, lat, deltat, ra2000, dec2000, distance, rv, deltara, deltadec, time)
    ! Returns the time of a star's rising and setting
    double precision, intent(in)  :: jday ! Julian Day under consideration
    double precision, intent(in)  :: lon  ! observer's geographical longitude, in degrees
    double precision, intent(in)  :: lat  ! observer's geographical latitude, in degrees
    double precision, intent(in)  :: deltat ! difference between universal time and dynamical time
    double precision, intent(in)  :: ra2000 ! right ascension at J2000.0
    double precision, intent(in)  :: dec2000 ! declination at J2000.0
    double precision, intent(in)  :: distance ! distance from the sun, in parsecs
    double precision, intent(in)  :: rv ! radial velocity, in parsecs per year
    double precision, intent(in)  :: deltara ! RA component of proper motion, in ARCSECONDS
    double precision, intent(in)  :: deltadec ! Dec component of proper motion, in ARCSECONDS
    double precision, dimension(2), intent(out) :: time ! time of sunrise and sunset
    call stellar_riset(jday, lon, lat, deltat, ra2000, dec2000, distance, rv, deltara, deltadec, time)
  end subroutine pub_stellar_riset

  subroutine pub_propmot(jday, ra, dec, distance, rv, dra, ddec, answer)
    ! Returns the proper motion of a star
    double precision, intent(in)  :: jday
    double precision, intent(in)  :: ra
    double precision, intent(in)  :: dec
    double precision, intent(in)  :: distance
    double precision, intent(in)  :: rv
    double precision, intent(in)  :: dra
    double precision, intent(in)  :: ddec
    double precision, dimension(2), intent(out) :: answer
    call propmot(jday, ra, dec, distance, rv, dra, ddec, answer)
  end subroutine pub_propmot

  subroutine pub_nutation(jday, nut)
    ! Returns the nutation at a given time
    double precision, intent(in)  :: jday
    double precision, dimension(0:2), intent(out) :: nut
    call nutation(jday, nut)
  end subroutine pub_nutation

  subroutine pub_solar_radec(jday, radec)
    ! Returns the right ascension and declination of the sun at a given time
    double precision, intent(in)  :: jday
    double precision, dimension(2), intent(out) :: radec
    call solar_radec(jday, radec)
  end subroutine pub_solar_radec

  subroutine pub_precession(jday, ra2000, dec2000, distance, rv, deltara, deltadec, answer)
    ! Return the precession at a given time
    double precision, intent(in)  :: jday
    double precision, intent(in)  :: ra2000
    double precision, intent(in)  :: dec2000
    double precision, intent(in)  :: distance
    double precision, intent(in)  :: rv
    double precision, intent(in)  :: deltara
    double precision, intent(in)  :: deltadec
    double precision, dimension(2), intent(out) :: answer
    call precession(jday, ra2000, dec2000, distance, rv, deltara, deltadec, answer)
  end subroutine pub_precession
end module pub

