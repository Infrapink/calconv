module sidereal
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
    double precision, intent(in) :: distance ! distance from the sun, in PARSECS
    double precision, intent(in) :: rv ! radial velocity, in PARSECS PER YEAR
    double precision, intent(in) :: deltara ! right ascension component of proper motion, in ARCSECONDS. This has to be looked up
    double precision, intent(in) :: deltadec ! declination component of proper motion, in SECONDS OF TIME. This has to be looked up.
    double precision, dimension(2), intent(out) :: answer
    
    ! double precision :: ra ! right ascension at the time of interest
    ! double precision :: dec ! declination at the time of interest

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

    pi = 4.0 * atan(1.0)
    d2r = pi / 180.0 ! convert degrees to radians
    r2d = 180.0 / pi ! convert radians to degrees

    x = distance * cos(dec2000 * d2r) * cos(ra2000 * d2r)
    y = distance * cos(dec2000 * d2r) * sin(ra2000 * d2r)
    z = distance * sin(dec2000 * d2r)
    !print *, x, y, z

    xdelta = ((x / distance) * rv) - (z * deltadec * cos(ra2000 * d2r)) - (y * deltara)
    ydelta = ((y / distance) * rv) - (z * deltadec * sin(ra2000 * d2r)) + (x * deltara)
    zdelta = ((z / distance) * rv) + (distance * deltadec * cos(dec2000 * d2r))

    t = (jday - 2451545.0) / 365.25 ! julian years since the year 2000 began at Greenwich Observatory

    xprime = x + (t * xdelta)
    yprime = y + (t * ydelta)
    zprime = z + (t * zdelta)

    answer(1) = atan(yprime / xprime) * r2d ! final mean right ascension as of t Julian years since J2000.0

    u = sqrt((xprime * xprime) + (yprime * yprime))
    answer(2) = atan(zprime / u) * r2d ! final mean declination as of t Julian years since J2000.0

    !print *, ra
    !print *, dec
    !answer(1) = ra
    !answer(2) = dec
  end subroutine propmot

  subroutine precession(jday, ra2000, dec2000, distance, rv, deltara, deltadec, answer)
    ! apply the effect of precession to obtain the actual right ascension and declination

    double precision, intent(in) :: jday ! Julian Day in question
    double precision, intent(in) :: ra2000 ! right ascension at J2000.0, in DEGREES
    double precision, intent(in) :: dec2000 ! declination at J2000.0, in DEGREES
    double precision, intent(in) :: distance ! distance from the sun, in PARSECS
    double precision, intent(in) :: rv ! radial velocity, in parsecs per year
    double precision, intent(in) :: deltara ! right ascension component of proper motion, in ARCSECONDS. This has to be looked up
    double precision, intent(in) :: deltadec ! declination component of proper motion,m in ARCSECONDS. This has to be looked up.
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

    pi = 4.0 * atan(1.0)
    d2r = pi / 180.0
    r2d = 180.0 / pi

    !print *, jday, ra2000, dec2000, distance, rv, deltara, deltadec
    !if (distance /= 0) then
    call propmot(jday, ra2000, dec2000, distance, rv, deltara, deltadec, radec)
    !end if
    ra = radec(1)
    dec = radec(2)

    t = (jday - 2451545.0) / 36525.0

    zeta = (2306.2181 * t) + (0.30188 * t * t) + (0.017998 * (t ** 3))
    z = (2306.2181 * t) + (1.09468 * t * t) + (0.018203 * (t ** 3))
    theta = (2004.3109 * t) + (0.42665 * t * t) + (0.041833 * (t ** 3))

    ! zeta, z, and theta are in ARCSECONDS, and so need to be converted into radians for the next bit
    zeta = (zeta / 3600.0) * d2r
    z = (z / 3600.0) * d2r
    theta = (theta / 3600.0) * d2r

    a = cos(dec) * sin(ra + zeta)
    b = (cos(theta) * cos(dec) * cos(ra + zeta)) - (sin(theta) * sin(dec))
    c = (sin(theta) * cos(dec) * cos(ra + zeta)) + (cos(theta) * sin(dec))

    answer(1) = z + (r2d * atan(a / b)) ! right ascension, in degrees, taking both proper motion and precession into accont
    answer(2) = r2d * asin(c) ! declination, in degrees, taking both proper motion and precession into account
    
  end subroutine precession

  subroutine nutation(jday, nut)
    ! Calculate the nutation of the obliquity to the ecplitic
    double precision, intent(in) :: jday ! Julian Day in question
    double precision, dimension(2), intent(out) :: nut ! Nutation to the ecliptic and of longitude

    double precision :: T ! Julian Centuries since J2000.0
    double precision :: D ! mean elonation of the moon from the sun
    double precision :: M ! mean anomaly of the sun
    double precision :: Mprime ! mean anomaly of the moon
    double precision :: F ! moon's argument of latitude
    double precision :: omega ! longitude of the ascending node of the moon's mean orbit on the ecliptic

    double precision, dimension(63,5) :: args
    double precision, dimension(63,2) :: psi_coeffs
    double precision, dimension(63,2) :: eps_coeffs
    double precision :: epsilon0 ! mean obliquity of the ecliptic, in degrees
    double precision :: delta_epsilon ! variation in the obliquity of the ecliptic, in arcseconds
    double precision :: delta_psi ! nutation in longitude, in arcseconds
    double precision :: U ! Julian Decamillennia since J2000.0

    integer :: i
    !double precision :: a ! placeholder

    double precision :: pi
    double precision :: d2r ! convert degrees to radians
    double precision :: r2d ! convert radians to degrees

    pi = 4.0 * atan(1.0)
    d2r = 180.0 / pi
    r2d = pi / 180.0

    T = (jday - 2451545.0) / 36525.0 ! time since J2000.0 in Julian centuries
    D = 297.85036 + (445267.111480 * T) - (0.00191427 * T * T) + ((T ** 3) / 189242.0)    ! mean elongation of the moon from the sun
    M = 357.52772 + (35999.0503407 * T) - (0.0001603 * T * T) - ((T ** 3) / 300000.0)     ! mean anomaly of the sun (Earth)
    Mprime = 134.96298 + (477198.867398 * T) + (0.0086972 * T * T) + ((T ** 3) / 56250.0) ! mean anomaly of the moon
    F = 93.27191 + (483202.017538 * T) - (0.0036825 * T * T) + ((T ** 3) / 327270.0)      ! moon's argument of latitude
    omega = 125.04452 - (1934.136261 * T) + (0.0020708 * T * T) + ((T ** 3) / 450000.0)   ! longitude of the moon's ascending node

    args( 1,:) = [ 0.0, 0.0, 0.0, 0.0, 1.0]
    args( 2,:) = [-2.0, 0.0, 0.0, 2.0, 2.0]
    args( 3,:) = [ 0.0, 0.0, 0.0, 2.0, 2.0]
    args( 4,:) = [ 0.0, 0.0, 0.0, 0.0, 2.0]
    args( 5,:) = [ 0.0, 1.0, 0.0, 0.0, 0.0]
    args( 6,:) = [ 0.0, 0.0, 1.0, 0.0, 0.0]
    args( 7,:) = [-2.0, 1.0, 0.0, 2.0, 2.0]
    args( 8,:) = [ 0.0, 0.0, 0.0, 2.0, 1.0]
    args( 9,:) = [ 0.0, 0.0, 1.0, 2.0, 2.0]
    args(10,:) = [-2.0,-1.0, 0.0, 2.0, 2.0]
    args(11,:) = [-2.0, 0.0, 1.0, 0.0, 0.0]
    args(12,:) = [-2.0, 0.0, 0.0, 2.0, 1.0]
    args(13,:) = [ 0.0, 0.0,-1.0, 2.0, 2.0]
    args(14,:) = [ 2.0, 0.0, 0.0, 0.0, 0.0]
    args(15,:) = [ 0.0, 0.0, 1.0, 0.0, 0.0]
    args(16,:) = [ 2.0, 0.0,-1.0, 2.0, 2.0]
    args(17,:) = [ 0.0, 0.0,-1.0, 0.0, 1.0]
    args(18,:) = [ 0.0, 0.0, 1.0, 2.0, 1.0]
    args(19,:) = [-2.0, 0.0, 2.0, 0.0, 0.0]
    args(20,:) = [ 0.0, 0.0,-2.0, 2.0, 1.0]
    args(21,:) = [ 2.0, 0.0, 0.0, 2.0, 2.0]
    args(22,:) = [ 0.0, 0.0, 2.0, 2.0, 2.0]
    args(23,:) = [ 0.0, 0.0, 2.0, 0.0, 0.0]
    args(24,:) = [-2.0, 0.0, 1.0, 2.0, 2.0]
    args(25,:) = [ 0.0, 0.0, 0.0, 2.0, 0.0]
    args(26,:) = [-2.0, 0.0, 0.0, 2.0, 0.0]
    args(27,:) = [ 0.0, 0.0,-1.0, 2.0, 1.0]
    args(28,:) = [ 0.0, 2.0, 0.0, 0.0, 0.0]
    args(29,:) = [ 2.0, 0.0,-1.0, 0.0, 1.0]
    args(30,:) = [-2.0, 2.0, 0.0, 2.0, 2.0]
    args(31,:) = [ 0.0, 1.0, 0.0, 0.0, 1.0]
    args(32,:) = [-2.0, 0.0, 1.0, 0.0, 1.0]
    args(33,:) = [ 0.0,-1.0, 0.0, 0.0, 1.0]
    args(34,:) = [ 0.0, 0.0, 2.0,-2.0, 0.0]
    args(35,:) = [ 2.0, 0.0,-1.0, 2.0, 1.0]
    args(36,:) = [ 2.0, 0.0, 1.0, 2.0, 2.0]
    args(37,:) = [ 0.0, 1.0, 0.0, 2.0, 2.0]
    args(38,:) = [-2.0, 1.0, 1.0, 0.0, 0.0]
    args(39,:) = [ 0.0,-1.0, 0.0, 2.0, 2.0]
    args(40,:) = [ 2.0, 0.0, 0.0, 2.0, 1.0]
    args(41,:) = [ 2.0, 0.0, 1.0, 0.0, 0.0]
    args(42,:) = [-2.0, 0.0, 2.0, 2.0, 2.0]
    args(43,:) = [-2.0, 0.0, 1.0, 2.0, 1.0]
    args(44,:) = [ 2.0, 0.0,-2.0, 0.0, 1.0]
    args(45,:) = [ 2.0, 0.0, 0.0, 0.0, 1.0]
    args(46,:) = [ 0.0,-1.0, 1.0, 0.0, 0.0]
    args(47,:) = [-2.0,-1.0, 0.0, 2.0, 1.0]
    args(48,:) = [-2.0, 0.0, 0.0, 0.0, 1.0]
    args(49,:) = [ 0.0, 0.0, 2.0, 2.0, 1.0]
    args(50,:) = [-2.0, 0.0, 2.0, 0.0, 1.0]
    args(51,:) = [-2.0, 1.0, 0.0, 2.0, 1.0]
    args(52,:) = [ 0.0, 0.0, 1.0,-2.0, 0.0]
    args(53,:) = [-1.0, 0.0, 1.0, 0.0, 0.0]
    args(54,:) = [-2.0, 1.0, 0.0, 0.0, 0.0]
    args(55,:) = [ 1.0, 0.0, 0.0, 0.0, 0.0]
    args(56,:) = [ 0.0, 0.0, 1.0, 2.0, 0.0]
    args(57,:) = [ 0.0, 0.0,-2.0, 2.0, 2.0]
    args(58,:) = [-1.0,-1.0, 1.0, 0.0, 0.0]
    args(59,:) = [ 0.0, 1.0, 1.0, 0.0, 0.0]
    args(60,:) = [ 0.0,-1.0, 1.0, 2.0, 2.0]
    args(61,:) = [ 2.0,-1.0,-1.0, 2.0, 2.0]
    args(62,:) = [ 0.0, 0.0, 3.0, 2.0, 2.0]
    args(63,:) = [ 2.0,-1.0, 0.0, 2.0, 2.0]

    psi_coeffs( 1,:) = [-171996.0, -174.27]
    psi_coeffs( 2,:) = [ -13187.0,   -1.60]
    psi_coeffs( 3,:) = [  -2274.0,   -0.20]
    psi_coeffs( 4,:) = [   2062.0,    0.20]
    psi_coeffs( 5,:) = [   1426.0,   -3.40]
    psi_coeffs( 6,:) = [    712.0,    0.10]
    psi_coeffs( 7,:) = [   -517.0,    1.20]
    psi_coeffs( 8,:) = [   -386.0,   -0.40]
    psi_coeffs( 9,:) = [   -301.0,    0.0 ]
    psi_coeffs(10,:) = [    217.0,   -0.50]
    psi_coeffs(11,:) = [   -158.0,    0.0 ]
    psi_coeffs(12,:) = [    129.0,    0.10]
    psi_coeffs(13,:) = [    123.0,    0.0 ]
    psi_coeffs(14,:) = [     63.0,    0.0 ]
    psi_coeffs(15,:) = [     63.0,    0.10]
    psi_coeffs(16,:) = [    -59.0,    0.0 ]
    psi_coeffs(17,:) = [    -58.0,   -0.10]
    psi_coeffs(18,:) = [    -51.0,    0.0 ]
    psi_coeffs(19,:) = [     48.0,    0.0 ]
    psi_coeffs(20,:) = [     46.0,    0.0 ]
    psi_coeffs(21,:) = [    -38.0,    0.0 ]
    psi_coeffs(22,:) = [    -31.0,    0.0 ]
    psi_coeffs(23,:) = [     29.0,    0.0 ]
    psi_coeffs(24,:) = [     29.0,    0.0 ]
    psi_coeffs(25,:) = [     26.0,    0.0 ]
    psi_coeffs(26,:) = [    -22.0,    0.0 ]
    psi_coeffs(27,:) = [     21.0,    0.0 ]
    psi_coeffs(28,:) = [     17.0,   -0.10]
    psi_coeffs(29,:) = [     16.0,    0.0 ]
    psi_coeffs(30,:) = [    -16.0,    0.10]
    psi_coeffs(31,:) = [    -15.0,    0.0 ]
    psi_coeffs(32,:) = [    -13.0,    0.0 ]
    psi_coeffs(33,:) = [    -12.0,    0.0 ]
    psi_coeffs(34,:) = [     11.0,    0.0 ]
    psi_coeffs(35,:) = [    -10.0,    0.0 ]
    psi_coeffs(36,:) = [     -8.0,    0.0 ]
    psi_coeffs(37,:) = [      7.0,    0.0 ]
    psi_coeffs(38,:) = [     -7.0,    0.0 ]
    psi_coeffs(39,:) = [     -7.0,    0.0 ]
    psi_coeffs(40,:) = [     -7.0,    0.0 ]
    psi_coeffs(41,:) = [      6.0,    0.0 ]
    psi_coeffs(42,:) = [      6.0,    0.0 ]
    psi_coeffs(43,:) = [      6.0,    0.0 ]
    psi_coeffs(44,:) = [     -6.0,    0.0 ]
    psi_coeffs(45,:) = [     -6.0,    0.0 ]
    psi_coeffs(46,:) = [      5.0,    0.0 ]
    psi_coeffs(47,:) = [     -5.0,    0.0 ]
    psi_coeffs(48,:) = [     -5.0,    0.0 ]
    psi_coeffs(49,:) = [     -5.0,    0.0 ]
    psi_coeffs(50,:) = [      4.0,    0.0 ]
    psi_coeffs(51,:) = [      4.0,    0.0 ]
    psi_coeffs(52,:) = [      4.0,    0.0 ]
    psi_coeffs(53,:) = [     -4.0,    0.0 ]
    psi_coeffs(54,:) = [     -4.0,    0.0 ]
    psi_coeffs(55,:) = [     -4.0,    0.0 ]
    psi_coeffs(56,:) = [      3.0,    0.0 ]
    psi_coeffs(57,:) = [     -3.0,    0.0 ]
    psi_coeffs(58,:) = [     -3.0,    0.0 ]
    psi_coeffs(59,:) = [     -3.0,    0.0 ]
    psi_coeffs(60,:) = [     -3.0,    0.0 ]
    psi_coeffs(61,:) = [     -3.0,    0.0 ]
    psi_coeffs(62,:) = [     -3.0,    0.0 ]
    psi_coeffs(63,:) = [     -3.0,    0.0 ]


    eps_coeffs = 0.0
    eps_coeffs( 1,:) = [92025.0, 8.9]
    eps_coeffs( 2,:) = [ 5736.0,-3.1]
    eps_coeffs( 3,:) = [  977.0,-0.5]
    eps_coeffs( 4,:) = [ -895.0, 0.5]
    eps_coeffs( 5,:) = [   54.0,-0.1]
    eps_coeffs( 6,:) = [   -7.0, 0.0]
    eps_coeffs( 7,:) = [  224.0,-0.6]
    eps_coeffs( 8,:) = [  200.0, 0.0]
    eps_coeffs( 9,:) = [  129.0,-0.1]
    eps_coeffs(10,:) = [  -95.0, 0.3]
    eps_coeffs(12,1) = -70.0
    eps_coeffs(13,1) = -53.0
    eps_coeffs(15,1) = -33.0
    eps_coeffs(16,1) =  26.0
    eps_coeffs(17,1) =  32.0
    eps_coeffs(18,1) =  27.0
    eps_coeffs(20,1) = -24.0
    eps_coeffs(21,1) =  16.0
    eps_coeffs(22,1) =  13.0
    eps_coeffs(24,1) = -12.0
    eps_coeffs(27,1) = -10.0
    eps_coeffs(29,1) =  -8.0
    eps_coeffs(30,1) =   7.0
    eps_coeffs(31,1) =   9.0
    eps_coeffs(32,1) =   7.0
    eps_coeffs(33,1) =   6.0
    eps_coeffs(35,1) =   5.0
    eps_coeffs(36,1) =   3.0
    eps_coeffs(37,1) =  -3.0
    eps_coeffs(39,1) =   3.0
    eps_coeffs(40,1) =   3.0
    eps_coeffs(42,1) =  -3.0
    eps_coeffs(43,1) =  -3.0
    eps_coeffs(44,1) =   3.0
    eps_coeffs(45,1) =   3.0
    eps_coeffs(47,1) =   3.0
    eps_coeffs(48,1) =   3.0
    eps_coeffs(49,1) =   3.0
    
    delta_epsilon = 0.0
    delta_psi = 0.0

    ! compute delta_epsilon, for the nutation in longitude
    do i = 1, 63
       delta_psi = delta_psi + ( (psi_coeffs(i,1) + (psi_coeffs(i,2) * T)) * sin(d2r * ( (args(i,1) * D) + (args(i,2) * M) + (args(i,3) * Mprime) + (args(i,4) * F) + (args(i,5) * omega)) ) ) ! nutation in longitude
       delta_epsilon = delta_epsilon + ( (eps_coeffs(i,1) + (eps_coeffs(i,2) * T)) * cos(d2r * ( (args(i,1) * D) + (args(i,2) * M) + (args(i,3) * Mprime) + (args(i,4) * F) + (args(i,5) * omega) ) ) ) ! nutation in obliquity
    end do

    ! Convert delta_epsilon and delta_psi into arcseconds
    delta_epsilon = delta_epsilon / 10000.0
    delta_psi = delta_psi / 10000.0 

    U = T / 100.0 ! Julian decamillennia since J2000.0
    epsilon0 = (23.0 * 3600.0) + (26.0 * 60.0) + 21.448 ! epsilon0, expressed in ARCSECONDS
    epsilon0 = epsilon0 - (4680.93 * U)
    epsilon0 = epsilon0 - (1.55 * (U ** 2))
    epsilon0 = epsilon0 + (1999.25 * (U ** 3))
    epsilon0 = epsilon0 - (51.38 * (U ** 4))
    epsilon0 = epsilon0 - (249.67 * (U ** 5))
    epsilon0 = epsilon0 - (39.05 * (U ** 6))
    epsilon0 = epsilon0 + (7.12 * (U ** 7))
    epsilon0 = epsilon0 + (27.87 * (U ** 8))
    epsilon0 = epsilon0 + (5.79 * (U ** 9))
    epsilon0 = epsilon0 + (2.45 * (U ** 10))

    epsilon0 = epsilon0 + delta_epsilon ! true obliquity
    !epsilon0 = mod(epsilon0, 26.0) ! if the obliquity of the ecliptic is calculated more than 10,000 years from J2000.0. the numbers become silly. This keeps it within sensible boundaries.
    ! nut = (epsilon0, delta_psi)
    nut(1) = epsilon0 / 3600.0  ! divide by 3600 to convert from seconds to degrees
    nut(2) = delta_psi / 3600.0 ! divide by 3600 to convert from seconds to degrees
  end subroutine nutation

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
    double precision, dimension(2) :: epsi ! nutation factors
    double precision :: d2r ! convert degrees to radians

    T = (jday - 2451545.0) / 36525.0
    midnight = 100.46061837 + (36000.770053608 * T) + (0.000387933 * T * T) - ((T ** 3) / 38710000.0) ! mean sidereal time at midnight at Greenwich, expressed in DEGREES.
    !alpha = inst * 1.00273790935
    !theta = midnight + alpha

    ! correct for true sidereal time
    d2r = (4.0 * atan(1.0)) / 180.0
    call nutation(jday, epsi)
    corr = epsi(2) * cos(d2r * epsi(1))
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
    double precision :: d2r = (4.0 * atan(1.0)) / 180.0 ! convert degrees to radians
    double precision :: T ! Julian centuries since epoch
    double precision, dimension(2) :: epsi ! nutation figures
    
    T = (jday - 2451545.0) / 36525.0
    answer = 280.46061837 + (360.98564736629 * T * 36525.0) + (0.000387933 * (T ** 2)) - ((T ** 3) / 38710000.0) ! mean sidereal time at jday, in DEGREES

    !d2r = (4.0 * atan(1.0)) / 180 ! convert degrees to radians
    call nutation(jday, epsi)
    answer = answer + (epsi(2) * cos(d2r * epsi(2)))
  end subroutine sidstant

  subroutine riset(jday, lon, lat, deltat, ra2000, dec2000, distance, rv, deltara, deltadec, id, time)
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
    integer, intent(in) :: id !What is actually rising or setting?
    double precision, dimension(2), intent(out) :: time ! time of sunrise and sunset, in days and fractions of a day
    
    double precision :: pi
    double precision :: d2r ! convert degrees to radians
    double precision :: r2d ! convert radians to degrees

    double precision :: h0 ! standard altitude, in degrees    
    double precision :: testval ! initial check
    ! double precision :: approx ! approximate time related to sunset

    double precision :: sid ! Sidereal time at midnight on the day in question
    double precision :: bigh
    
    double precision :: nr ! used in calculating a modification to the rise time
    double precision :: ns ! used in calculating a modification to the set time
    double precision :: a_ra ! used in calculating interpolation
    double precision :: b_ra ! used in calculating interpolation
    double precision :: c_ra  ! used in calculating interpolation
    double precision :: a_dec ! used in calculating interpolation
    double precision :: b_dec ! used in calculating interpolation
    double precision :: c_dec ! used in calculating interpolation
    double precision :: rai_r ! right ascension, interpolated, for sunrise
    double precision :: deci_r ! declination, interpolated, for sunrise
    double precision :: rai_s ! right ascension, interpolated, for sunset
    double precision :: deci_s ! declination, interpolated, for sunset
    ! double precision, dimension(2) :: inr ! interpolated RA and dec for sunrise
    ! double precision, dimension(2) :: ins ! interpolated RA and dec for sunset
    double precision :: alt_r ! altitude at sunrise
    double precision :: alt_s ! altitude at sunset
    double precision :: ha_r ! hour angle of rising sun, in degrees
    double precision :: ha_s ! hour angle of setting sun, in degrees
    
    double precision :: transit ! time the sun crosses the meridian
    double precision :: theta_r ! sidereal time of the sunrise converted into degrees
    double precision :: theta_s ! sidereal time of the sunset converted into degrees

    double precision :: delta_r ! modification to get true rising time
    double precision :: delta_s ! modification to get true setting time

    double precision, dimension(2) :: yesterday ! RA and dec of prev day
    double precision, dimension(2) :: today ! RA and dec of day
    double precision, dimension(2) :: tomorrow ! RA and dec of next day
    
    pi = 4.0 * atan(1.0)
    d2r = pi / 180.0
    r2d = 180.0 / pi

    !print *, jday, lon, lat, deltat, ra2000, dec2000, distance, rv, deltara, deltadec, id

    if (id == 0) then
       ! It's the sun
       h0 = -50.0 / 60.0 ! this is in degrees, not radians
    else
       ! It's a star or a planet
       h0 = -34.0 / 60.0 ! this is in degrees, not radians
    end if
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

    bigh = (sin(d2r * h0) - (sin(d2r * lat) * sin(d2r * today(2)))) / (cos(d2r * lat) * cos(today(2)))
    if (abs(bigh) > 1.0) then
       time = 25.0
    else
       bigh = acos(bigh)

       call getsid(jday, sid)
       
       transit = (tomorrow(1) + lon - sid) / 360.0
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

       !call getsid(jday, sid)

       theta_r = sid + (360.985647 * time(1))
       theta_s = sid + (360.985647 * time(2))

       nr = time(1) + (deltat / 86400.0)
       ns = time(2) + (deltat / 86400.0)

       ! interpolation

       ! RA interpolation
       a_ra = today(1) - yesterday(1)
       b_ra = tomorrow(1) - today(1)
       c_ra = b_ra - a_ra
       rai_r = (nr / 2.0) * (a_ra + b_ra + (nr * c_ra))
       rai_s = (ns / 2.0) * (a_ra + b_ra + (ns * c_ra))

       ! dec interpolation
       a_dec = today(2) - yesterday(2)
       b_dec = tomorrow(2) - today(2)
       c_dec = b_dec - a_dec
       deci_r = (nr / 2.0) * (a_dec + b_dec + (nr * c_dec))
       deci_s = (ns / 2.0) * (a_dec + b_dec + (ns * c_dec))

       ha_r = theta_r - lon - rai_r
       ha_s = theta_s - lon - rai_s       

       alt_r = r2d * asin((sin(d2r * lat) * sin(d2r * deci_r)) + (cos(d2r * lat) * cos(ha_r)))
       alt_s = r2d * asin((sin(d2r * lat) * sin(d2r * deci_r)) + (cos(d2r * lat) * cos(ha_r)))

       ! MAKE SURE alt IS IN DEGREES. IF NOT, BE SURE TO CORRECT IT.

       delta_r = (alt_r - h0) / (360.0 * cos(deci_r * d2r) * cos(lat * d2r) * sin(bigh))
       delta_s = (alt_s - h0) / (360.0 * cos(deci_s * d2r) * cos(lat * d2r) * sin(bigh))

       time(1) = time(1) + delta_r
       time(2) = time(2) + delta_s

       ! time(x) now gives the fraction of a day that has elapsed since midnight when the body rises (x == 1) or sets (x == 2)
       ! these can be compared to floats, Fractions, and Decimals in Python, but might need to be converted into other units
       ! multiply time(x) by 24 to get the time in hours (which will still have a decimal portion; for example, 06:30 would register as 6.5)
       ! multiply time(x) by 1440 to get the time in minutes, or by 86400 to get the time in seconds.
       ! time(x) can even be multiplied by 25920 to get the time in chalakim.
    end if
    !print *, time
  end subroutine riset
end module sidereal
