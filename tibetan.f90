module tibetan
  ! subroutines for computing time in Tibetan calendars
  ! Kalachakra Tantra and the Tibetan calendar by Edward Henning, American Institute of Buddhist Studies, New York, 2007 AD
  ! Tibetan Calendar Mathematics, Svante Janson, 24 January 2014 AD

  ! The most widely-cited and well-regarded textbook on Tibetan calendars is Diter Schuh's
  ! Untersuchungen zur Geschichte der Tibetischen Kalenderrechnung. Franz Steiner Verlag, Wiesbaden, 1973
  ! Unfortunately, I don't speak German, so I can't consult it.
  implicit none

contains

  subroutine normalise(numerators, denominators, answer)
    ! given two arrays representing a number in mixed-radix notation and the denominators thereof respectively,
    ! reduce to a proper fraction
    ! all arrays passed must be of dimension 6
    integer, dimension(6), intent(in)  :: numerators
    integer, dimension(6), intent(in)  :: denominators
    integer, dimension(6), intent(out) :: answer

    integer :: i ! counting placeholder

    answer = numerators
    do i = 6, 2, (-1)
       answer(i - 1) = answer(i - 1) + (answer(i) / denominators(i))
       answer(i) = modulo(answer(i), denominators(i))
    end do
    !print *, answer
  end subroutine normalise

  subroutine reduce(numerators, denominators, answer)
    ! basically do modulo arithmetic with two arrays
    integer, dimension(6), intent(in)  :: numerators
    integer, dimension(6), intent(in)  :: denominators
    integer, dimension(6), intent(out) :: answer

    call normalise(numerators, denominators, answer)
    answer(1) = modulo(answer(1), denominators(1))
  end subroutine reduce

  subroutine phugpa(mcount, tithi, jday)
    ! compute the time since the epoch that a given tithi begins
    ! tithi numbering begins at 0
    ! the end of tithi (N - 1) corresponds to the start of tithi N
    integer, intent(in)  :: mcount ! whole months since the epoch
    integer, intent(in)  :: tithi  ! lunar "days" since new moon
    integer, dimension(0:5), intent(out) :: jday ! time since the epoch as of the end of tithi

    ! arrays used in computing the mean weekday
    integer, dimension(0:5) :: w0
    integer, dimension(0:5) :: w1 ! synodic month
    integer, dimension(0:5) :: w2
    integer, dimension(0:5) :: w3
    !integer, dimension(0:5) :: jday ! mean weekday
    integer, dimension(0:5) :: adj ! amount to adjust by to get the semi-true weekday and true solar longitude

    ! arrays used in computing the mean solar longitude
    integer, dimension(0:5) :: s0
    integer, dimension(0:5) :: s1
    integer, dimension(0:5) :: s2
    integer, dimension(0:5) :: s3
    integer, dimension(0:5) :: msl ! mean solar longitude

    integer :: i ! counting placeholder
    integer :: k ! placeholder
    integer :: n ! placeholder

    integer, dimension(0:1) :: anomaly
    integer :: aq
    integer :: ar
    logical :: hc ! half-circle; used to note whether a half-circle is deducted from the mean solar longitude later.

    integer, dimension(0:13,0:1) :: ANOM_TABLE !Henning's Table 1-1
    integer, dimension( 0:5,0:1) :: SOLAR_TABLE !Henning's Table 1-2

    ! Henning's Table 1-1, p. 24
    ANOM_TABLE( 0,:) = [5, 0]
    ANOM_TABLE( 1,:) = [5, 5]
    ANOM_TABLE( 2,:) = [5,10]
    ANOM_TABLE( 3,:) = [5,15]
    ANOM_TABLE( 4,:) = [4,19]
    ANOM_TABLE( 5,:) = [3,22]
    ANOM_TABLE( 6,:) = [2,24]
    ANOM_TABLE( 7,:) = [1,25]
    ANOM_TABLE( 8,:) = [1,24]
    ANOM_TABLE( 9,:) = [2,22]
    ANOM_TABLE(10,:) = [3,19]
    ANOM_TABLE(11,:) = [4,15]
    ANOM_TABLE(12,:) = [5,10]
    ANOM_TABLE(13,:) = [5, 5]

    ! Henning's Table 1-2, p. 33
    SOLAR_TABLE(0,:) = [6, 0]
    SOLAR_TABLE(1,:) = [6, 6]
    SOLAR_TABLE(2,:) = [4,10]
    SOLAR_TABLE(3,:) = [1,11]
    SOLAR_TABLE(4,:) = [1,10]
    SOLAR_TABLE(5,:) = [4, 6]

    ! Compute the mean weekday
    ! This part comes from Henning, p. 18,23
    w0 = [      7, 60, 60, 6, 707, 707]
    w1 = [     29, 31, 50, 0, 480,   0] ! synodic month
    w2 = [2424972, 57, 53, 2,  20,   0] ! lunar epoch in Julian Days
    w3 = [      0, 59,  3, 4,  16,   0] ! length of a tithi in solar days
    jday = (mcount * w1) + w2 + (tithi * w3)
    call normalise(jday, w0, jday)

    ! Compute the anomaly
    ! Henning, p. 21
    anomaly = (mcount * [2,1]) + [13,103]
    anomaly(0) = anomaly(0) + (anomaly(1) / 126)
    anomaly(1) = modulo(anomaly(1), 126)
    anomaly(0) = modulo(anomaly(0),  28)

    ! Compute the mean solar longitude
    ! Henning, p. 22-23
    s0  = [27, 60, 60, 6, 67, 707]
    s1  = [ 2, 10, 58, 1, 17,   0] ! distance the sun travels in a synodic month, measured in nakshatras
    s2  = [25,  9, 10, 4, 32,   0] ! sun's zodiacal longitude at epoch, measured in nakshatras
    s3  = [ 0,  4, 21, 5, 43,   0] ! distance the sun travels in a tithi, measured in nakshatras
    msl = (mcount * s1) + s2 + (tithi * s3)
    call reduce(msl, s0, msl)

    ! Compute the semi-true weekday
    ! See Henning, p. 24-26
    aq = (anomaly(0) + tithi) / 14
    ar = modulo((anomaly(0) + tithi), 14)
    adj = 0
    n = ((anomaly(1) * 30) + tithi) * ANOM_TABLE(modulo((ar + 1), 14), 0)
    adj(1) = ANOM_TABLE(ar, 1) + (n / 3780)
    do i = 2, 4, 1
       n = modulo(n, 3780)
       n = n * w0(i)
       adj(i) = n / 3780
    end do
    call normalise(jday, w0, jday)
    if (modulo(aq, 2) == 1) then
       jday = jday - adj
    else
       jday = jday + adj
    end if

    ! compute the true weekday and solar longitude.
    ! First, make jday compatible with msl
    ! See Henning, p. 31
    call normalise(jday, w0, jday)
    jday(5) = modulo((jday(4) * 67), 707)
    jday(4) = (jday(4) * 67) / 707
    call normalise(jday, s0, jday)

    ! adjust msl
    ! Henning, p. 31-34
    msl(0) = modulo(msl(0), 27)
    msl = msl - [6, 45, 0, 0, 0, 0]
    call reduce(msl, s0, msl)
    if ( (msl(0) > 14) .or. ( (msl(0) == 13) .and. (msl(1) >= 30) ) ) then
       hc = .true.
       msl = msl - [13, 30, 0, 0, 0, 0]
       call reduce(msl, s0, msl)
    else
       hc = .false.
    end if
    n = (msl(0) * 60) + msl(1)
    adj = [0, modulo(n, 135), msl(2), msl(3), msl(4), msl(5)]
    k = (((((adj(1) * 60) + adj(2)) * 6) + adj(3)) * 67) + adj(4) ! Henning, p. 34
    i = modulo(n, 135) + 1
    i = modulo(i, 6)
    k = k * SOLAR_TABLE(i, 1)
    adj = 0
    do i = 4, 1, (-1)
       adj(i) = modulo(k, s0(i))
       k = k / s0(i)
    end do
    k = 0
    do i = 1, 4, 1
       k = k + adj(i)
       adj(i) = k / 135
       k = (modulo(k, 135) * s0(i + 1)) + adj(i + 1)
    end do
    if (modulo(n, 6) < 3) then
       adj = [0, modulo(n, 6), 0, 0, 0, 0] + adj
    else
       adj = [0, modulo(n, 6), 0, 0, 0, 0] - adj
    end if
    call reduce(adj, s0, adj)

    ! apply adj to jday and msl to get the true "weekday" and solar longitude
    ! See Henning, p. 35
    if (hc .eqv. .true.) then
       jday = jday + adj
       msl = msl + adj
    else
       jday = jday - adj
       msl = msl - adj
    end if
    call normalise(jday, s0, jday)
    call reduce(msl, s0, msl)
    
  end subroutine phugpa

  subroutine karana(mcount, tithi, jday)
    ! compute the time since the epoch that a given tithi begins
    ! tithi numbering begins at 0
    ! the end of tithi (N - 1) corresponds to the start of tithi N
    ! See Henning, Chapter 6, pp. 295—307
    ! Janson, Section A.6
    integer, intent(in)  :: mcount ! whole months since the epoch
    integer, intent(in)  :: tithi  ! lunar "days" since new moon
    integer, dimension(0:5), intent(out) :: jday ! time since the epoch as of the end of tithi

    ! arrays used in computing the mean weekday
    integer, dimension(0:5) :: w0
    integer, dimension(0:5) :: w1 ! synodic month
    integer, dimension(0:5) :: w2
    integer, dimension(0:5) :: w3
    integer, dimension(0:5) :: adj ! amount to adjust by to get the semi-true weekday and true solar longitude

    ! arrays used in computing the mean solar longitude
    integer, dimension(0:5) :: s0
    integer, dimension(0:5) :: s1
    integer, dimension(0:5) :: s2
    integer, dimension(0:5) :: s3
    integer, dimension(0:5) :: msl ! mean solar longitude

    integer :: i ! counting placeholder
    integer :: k ! placeholder
    integer :: n ! placeholder

    integer, dimension(0:1) :: anomaly
    integer :: aq
    integer :: ar
    logical :: hc ! half-circle; used to note whether a half-circle is deducted from the mean solar longitude later.

    integer, dimension(0:13,0:1) :: ANOM_TABLE !Henning's Table 1-1
    integer, dimension( 0:5,0:1) :: SOLAR_TABLE !Henning's Table 1-2

    ! Henning's Table 1-1, p. 24
    ANOM_TABLE( 0,:) = [5, 0]
    ANOM_TABLE( 1,:) = [5, 5]
    ANOM_TABLE( 2,:) = [5,10]
    ANOM_TABLE( 3,:) = [5,15]
    ANOM_TABLE( 4,:) = [4,19]
    ANOM_TABLE( 5,:) = [3,22]
    ANOM_TABLE( 6,:) = [2,24]
    ANOM_TABLE( 7,:) = [1,25]
    ANOM_TABLE( 8,:) = [1,24]
    ANOM_TABLE( 9,:) = [2,22]
    ANOM_TABLE(10,:) = [3,19]
    ANOM_TABLE(11,:) = [4,15]
    ANOM_TABLE(12,:) = [5,10]
    ANOM_TABLE(13,:) = [5, 5]

    ! Henning's Table 1-2, p. 33
    SOLAR_TABLE(0,:) = [6, 0]
    SOLAR_TABLE(1,:) = [6, 6]
    SOLAR_TABLE(2,:) = [4,10]
    SOLAR_TABLE(3,:) = [1,11]
    SOLAR_TABLE(4,:) = [1,10]
    SOLAR_TABLE(5,:) = [4, 6]

    ! Compute the mean weekday
    ! This part comes from Henning, p. 296
    w0 = [      7, 60, 60, 6, 707, 707]
    w1 = [     29, 31, 50, 0,   0,   0] ! synodic month
    w2 = [2015531, 31, 50, 0,   0,   0] ! lunar epoch in Julian Days
    w3 = [      0, 59,  3, 4,   0,   0] ! length of a tithi in solar days
    jday = (mcount * w1) + w2 + (tithi * w3)
    call normalise(jday, w0, jday)

    ! Compute the anomaly
    ! Henning, p. 296
    anomaly = (mcount * [2,1]) + [5,112]
    anomaly(0) = anomaly(0) + (anomaly(1) / 126)
    anomaly(1) = modulo(anomaly(1), 126)
    anomaly(0) = modulo(anomaly(0),  28)

    ! Compute the mean solar longitude
    ! Henning, p. 22-23, 296
    s0  = [27, 60, 60, 6, 13, 707]
    s1  = [ 2, 10, 58, 2, 10,   0] ! distance the sun travels in a synodic month, measured in nakshatras
    s2  = [26, 58,  0, 0,  0,   0] ! sun's zodiacal longitude at epoch, measured in nakshatras
    s3  = [ 0,  2,  9, 5,  9,   0] ! distance the sun travels in a tithi, measured in nakshatras
    msl = (mcount * s1) + s2 + (tithi * s3)
    call reduce(msl, s0, msl)

    ! Compute the semi-true weekday
    ! See Henning, p. 24-26
    aq = (anomaly(0) + tithi) / 14
    ar = modulo((anomaly(0) + tithi), 14)
    adj = 0
    n = ((anomaly(1) * 30) + tithi) * ANOM_TABLE(modulo((ar + 1), 14), 0)
    adj(1) = ANOM_TABLE(ar, 1) + (n / 3780)
    do i = 2, 4, 1
       n = modulo(n, 3780)
       n = n * w0(i)
       adj(i) = n / 3780
    end do
    call normalise(jday, w0, jday)
    if (modulo(aq, 2) == 1) then
       jday = jday - adj
    else
       jday = jday + adj
    end if
    ! jday should now represent the semi-true weekday

    ! compute the true weekday and solar longitude.
    ! First, make jday compatible with msl
    ! See Henning, p. 31
    call normalise(jday, w0, jday)
    jday(5) = modulo((jday(4) * 13), 707)
    jday(4) = (jday(4) * 67) / 707
    call normalise(jday, s0, jday)

    ! adjust msl
    ! Henning, p. 31-34
    msl(0) = modulo(msl(0), 27)
    msl = msl - [6, 45, 0, 0, 0, 0]
    call reduce(msl, s0, msl)
    if ( (msl(0) > 14) .or. ( (msl(0) == 13) .and. (msl(1) >= 30) ) ) then
       hc = .true.
       msl = msl - [13, 30, 0, 0, 0, 0]
       call reduce(msl, s0, msl)
    else
       hc = .false.
    end if
    n = (msl(0) * 60) + msl(1)
    adj = [0, modulo(n, 135), msl(2), msl(3), msl(4), msl(5)]
    k = (((((adj(1) * 60) + adj(2)) * 6) + adj(3)) * 13) + adj(4) ! Henning, p. 34
    i = modulo(n, 135) + 1
    i = modulo(i, 6)
    k = k * SOLAR_TABLE(i, 1)
    adj = 0
    do i = 4, 1, (-1)
       adj(i) = modulo(k, s0(i))
       k = k / s0(i)
    end do
    k = 0
    do i = 1, 4, 1
       k = k + adj(i)
       adj(i) = k / 135
       k = (modulo(k, 135) * s0(i + 1)) + adj(i + 1)
    end do
    if (modulo(n, 6) < 3) then
       adj = [0, modulo(n, 6), 0, 0, 0, 0] + adj
    else
       adj = [0, modulo(n, 6), 0, 0, 0, 0] - adj
    end if
    call reduce(adj, s0, adj)

    ! apply adj to jday and msl to get the true "weekday" and solar longitude
    ! See Henning, p. 35
    if (hc .eqv. .true.) then
       jday = jday + adj
       msl = msl + adj
    else
       jday = jday - adj
       msl = msl - adj
    end if
    call normalise(jday, s0, jday)
    call reduce(msl, s0, msl)
    
  end subroutine karana

  subroutine tsurphu(mcount, tithi, jday)
    ! compute the time since the epoch that a given tithi begins
    ! tithi numbering begins at 0
    ! the end of tithi (N - 1) corresponds to the start of tithi N
    ! See Henning, Chapter 6, pp. 337—342
    ! Janson, Section A.5
    integer, intent(in)  :: mcount ! whole months since the epoch
    integer, intent(in)  :: tithi  ! lunar "days" since new moon
    integer, dimension(0:5), intent(out) :: jday ! time since the epoch as of the end of tithi

    ! arrays used in computing the mean weekday
    integer, dimension(0:5) :: w0
    integer, dimension(0:5) :: w1 ! synodic month
    integer, dimension(0:5) :: w2
    integer, dimension(0:5) :: w3
    !integer, dimension(0:5) :: jday ! mean weekday
    integer, dimension(0:5) :: adj ! amount to adjust by to get the semi-true weekday and true solar longitude

    ! arrays used in computing the mean solar longitude
    integer, dimension(0:5) :: s0
    integer, dimension(0:5) :: s1
    integer, dimension(0:5) :: s2
    integer, dimension(0:5) :: s3
    integer, dimension(0:5) :: msl ! mean solar longitude

    integer :: i ! counting placeholder
    integer :: k ! placeholder
    integer :: n ! placeholder

    integer, dimension(0:1) :: anomaly
    integer :: aq
    integer :: ar
    logical :: hc ! half-circle; used to note whether a half-circle is deducted from the mean solar longitude later.

    integer, dimension(0:13,0:1) :: ANOM_TABLE !Henning's Table 1-1
    integer, dimension( 0:5,0:1) :: SOLAR_TABLE !Henning's Table 1-2

    ! Henning's Table 1-1, p. 24
    ANOM_TABLE( 0,:) = [5, 0]
    ANOM_TABLE( 1,:) = [5, 5]
    ANOM_TABLE( 2,:) = [5,10]
    ANOM_TABLE( 3,:) = [5,15]
    ANOM_TABLE( 4,:) = [4,19]
    ANOM_TABLE( 5,:) = [3,22]
    ANOM_TABLE( 6,:) = [2,24]
    ANOM_TABLE( 7,:) = [1,25]
    ANOM_TABLE( 8,:) = [1,24]
    ANOM_TABLE( 9,:) = [2,22]
    ANOM_TABLE(10,:) = [3,19]
    ANOM_TABLE(11,:) = [4,15]
    ANOM_TABLE(12,:) = [5,10]
    ANOM_TABLE(13,:) = [5, 5]

    ! Henning's Table 1-2, p. 33
    SOLAR_TABLE(0,:) = [6, 0]
    SOLAR_TABLE(1,:) = [6, 6]
    SOLAR_TABLE(2,:) = [4,10]
    SOLAR_TABLE(3,:) = [1,11]
    SOLAR_TABLE(4,:) = [1,10]
    SOLAR_TABLE(5,:) = [4, 6]

    ! Compute the mean weekday
    ! This part comes from Henning, p. 340 and Janson, Section A.2
    ! I'm using the 1852 AD epoch to avoid negative numbers
    w0 = [      7, 60, 60, 6, 13, 707]
    w1 = [     29, 31, 50, 0,  8, 584] ! synodic month
    w2 = [2397598,  9, 24, 2,  5,  14] ! lunar epoch in Julian Days
    w3 = [      0, 59,  3, 4,  0, 208] ! length of a tithi in solar days
    jday = (mcount * w1) + w2 + (tithi * w3)
    call normalise(jday, w0, jday)

    ! Compute the anomaly
    ! Henning, p. 21 and 340 and Janson, Section A.2
    anomaly = (mcount * [2,1]) + [0, 72]
    anomaly(0) = anomaly(0) + (anomaly(1) / 126)
    anomaly(1) = modulo(anomaly(1), 126)
    anomaly(0) = modulo(anomaly(0),  28)

    ! Compute the mean solar longitude
    ! Henning, p. 22—23, 340
    s0  = [27, 60, 60, 6, 13, 67]
    s1  = [ 2, 10, 58, 1,  3, 20] ! Nakshatras the sun travels in a mean synodic month
    s2  = [ 0,  1, 22, 2,  4, 18] ! Solar longitude at epoch, in nakshatras
    s3  = [ 0,  4, 21, 5,  8, 23] ! Distance the sun travels in a mean tithi
    msl = (mcount * s1) + s2 + (tithi * s3)
    call reduce(msl, s0, msl)

    ! Compute the semi-true weekday
    ! See Henning, p. 24-26
    aq = (anomaly(0) + tithi) / 14
    ar = modulo((anomaly(0) + tithi), 14)
    adj = 0
    n = ((anomaly(1) * 30) + tithi) * ANOM_TABLE(modulo((ar + 1), 14), 0)
    adj(1) = ANOM_TABLE(ar, 1) + (n / 3780)
    do i = 2, 4, 1
       n = modulo(n, 3780)
       n = n * w0(i)
       adj(i) = n / 3780
    end do
    call normalise(jday, w0, jday)
    if (modulo(aq, 2) == 1) then
       jday = jday - adj
    else
       jday = jday + adj
    end if

    ! compute the true weekday and solar longitude.
    ! First, make jday compatible with msl
    ! See Henning, p. 31
    call normalise(jday, w0, jday)
    jday(5) = (jday(5) * 707) / 67
    call normalise(jday, s0, jday)

    ! adjust msl
    ! Henning, p. 31-34
    msl(0) = modulo(msl(0), 27)
    msl = msl - [6, 45, 0, 0, 0, 0]
    call reduce(msl, s0, msl)
    if ( (msl(0) > 14) .or. ( (msl(0) == 13) .and. (msl(1) >= 30) ) ) then
       hc = .true.
       msl = msl - [13, 30, 0, 0, 0, 0]
       call reduce(msl, s0, msl)
    else
       hc = .false.
    end if
    n = (msl(0) * 60) + msl(1)
    adj = [0, modulo(n, 135), msl(2), msl(3), msl(4), msl(5)]
    k = (((((adj(1) * 60) + adj(2)) * 6) + adj(3)) * 67) + adj(4) ! Henning, p. 34
    i = modulo(n, 135) + 1
    i = modulo(i, 6)
    k = k * SOLAR_TABLE(i, 1)
    adj = 0
    do i = 4, 1, (-1)
       adj(i) = modulo(k, s0(i))
       k = k / s0(i)
    end do
    k = 0
    do i = 1, 4, 1
       k = k + adj(i)
       adj(i) = k / 135
       k = (modulo(k, 135) * s0(i + 1)) + adj(i + 1)
    end do
    if (modulo(n, 6) < 3) then
       adj = [0, modulo(n, 6), 0, 0, 0, 0] + adj
    else
       adj = [0, modulo(n, 6), 0, 0, 0, 0] - adj
    end if
    call reduce(adj, s0, adj)

    ! apply adj to jday and msl to get the true "weekday" and solar longitude
    ! See Henning, p. 35
    if (hc .eqv. .true.) then
       jday = jday + adj
       msl = msl + adj
    else
       jday = jday - adj
       msl = msl - adj
    end if
    call normalise(jday, s0, jday)
    call reduce(msl, s0, msl)
    
  end subroutine tsurphu

  subroutine mongolian(mcount, tithi, jday)
    ! compute the time since the epoch that a given tithi begins
    ! tithi numbering begins at 0
    ! the end of tithi (N - 1) corresponds to the start of tithi N
    integer, intent(in)  :: mcount ! whole months since the epoch
    integer, intent(in)  :: tithi  ! lunar "days" since new moon
    integer, dimension(0:5), intent(out) :: jday ! time since the epoch as of the end of tithi

    ! arrays used in computing the mean weekday
    integer, dimension(0:5) :: w0
    integer, dimension(0:5) :: w1 ! synodic month
    integer, dimension(0:5) :: w2
    integer, dimension(0:5) :: w3
    !integer, dimension(0:5) :: jday ! mean weekday
    integer, dimension(0:5) :: adj ! amount to adjust by to get the semi-true weekday and true solar longitude

    ! arrays used in computing the mean solar longitude
    integer, dimension(0:5) :: s0
    integer, dimension(0:5) :: s1
    integer, dimension(0:5) :: s2
    integer, dimension(0:5) :: s3
    integer, dimension(0:5) :: msl ! mean solar longitude

    integer :: i ! counting placeholder
    integer :: k ! placeholder
    integer :: n ! placeholder

    integer, dimension(0:1) :: anomaly
    integer :: aq
    integer :: ar
    logical :: hc ! half-circle; used to note whether a half-circle is deducted from the mean solar longitude later.

    integer, dimension(0:13,0:1) :: ANOM_TABLE !Henning's Table 1-1
    integer, dimension( 0:5,0:1) :: SOLAR_TABLE !Henning's Table 1-2

    ! Henning's Table 1-1, p. 24
    ANOM_TABLE( 0,:) = [5, 0]
    ANOM_TABLE( 1,:) = [5, 5]
    ANOM_TABLE( 2,:) = [5,10]
    ANOM_TABLE( 3,:) = [5,15]
    ANOM_TABLE( 4,:) = [4,19]
    ANOM_TABLE( 5,:) = [3,22]
    ANOM_TABLE( 6,:) = [2,24]
    ANOM_TABLE( 7,:) = [1,25]
    ANOM_TABLE( 8,:) = [1,24]
    ANOM_TABLE( 9,:) = [2,22]
    ANOM_TABLE(10,:) = [3,19]
    ANOM_TABLE(11,:) = [4,15]
    ANOM_TABLE(12,:) = [5,10]
    ANOM_TABLE(13,:) = [5, 5]

    ! Henning's Table 1-2, p. 33
    SOLAR_TABLE(0,:) = [6, 0]
    SOLAR_TABLE(1,:) = [6, 6]
    SOLAR_TABLE(2,:) = [4,10]
    SOLAR_TABLE(3,:) = [1,11]
    SOLAR_TABLE(4,:) = [1,10]
    SOLAR_TABLE(5,:) = [4, 6]

    ! Compute the mean weekday
    ! This part comes from Janson, section A.3
    w0 = [      7, 60, 60, 6, 67, 707]
    w1 = [     29, 31, 50, 0, 45, 345] ! synodic month
    w2 = [2359237, 55, 13, 3, 31, 394] ! lunar epoch in Julian Days
    w3 = [      0, 59,  3, 4,  1, 365] ! length of a tithi in solar days
    jday = (mcount * w1) + w2 + (tithi * w3)
    call normalise(jday, w0, jday)

    ! Compute the anomaly
    ! Henning, p. 21
    anomaly = (mcount * [2,1]) + [24,22]
    anomaly(0) = anomaly(0) + (anomaly(1) / 126)
    anomaly(1) = modulo(anomaly(1), 126)
    anomaly(0) = modulo(anomaly(0),  28)

    ! Compute the mean solar longitude
    ! Henning, p. 22-23
    ! Janson, section A.3
    s0  = [27, 60, 60, 6, 67, 707]
    s1  = [ 2, 10, 58, 1, 17,   0]
    s2  = [26, 39, 51, 0, 18,   0]
    s3  = [ 0,  4, 21, 5, 43,   0]
    msl = (mcount * s1) + s2 + (tithi * s3)
    call reduce(msl, s0, msl)

    ! Compute the semi-true weekday
    ! See Henning, p. 24-26
    aq = (anomaly(0) + tithi) / 14
    ar = modulo((anomaly(0) + tithi), 14)
    adj = 0
    n = ((anomaly(1) * 30) + tithi) * ANOM_TABLE(modulo((ar + 1), 14), 0)
    adj(1) = ANOM_TABLE(ar, 1) + (n / 3780)
    do i = 2, 4, 1
       n = modulo(n, 3780)
       n = n * w0(i)
       adj(i) = n / 3780
    end do
    call normalise(jday, w0, jday)
    if (modulo(aq, 2) == 1) then
       jday = jday - adj
    else
       jday = jday + adj
    end if

    call normalise(jday, w0, jday)

    ! adjust msl
    ! Henning, p. 31-34
    msl(0) = modulo(msl(0), 27)
    msl = msl - [6, 45, 0, 0, 0, 0]
    call reduce(msl, s0, msl)
    if ( (msl(0) > 14) .or. ( (msl(0) == 13) .and. (msl(1) >= 30) ) ) then
       hc = .true.
       msl = msl - [13, 30, 0, 0, 0, 0]
       call reduce(msl, s0, msl)
    else
       hc = .false.
    end if
    n = (msl(0) * 60) + msl(1)
    adj = [0, modulo(n, 135), msl(2), msl(3), msl(4), msl(5)]
    k = (((((adj(1) * 60) + adj(2)) * 6) + adj(3)) * 67) + adj(4) ! Henning, p. 34
    i = modulo(n, 135) + 1
    i = modulo(i, 6)
    k = k * SOLAR_TABLE(i, 1)
    adj = 0
    do i = 4, 1, (-1)
       adj(i) = modulo(k, s0(i))
       k = k / s0(i)
    end do
    k = 0
    do i = 1, 4, 1
       k = k + adj(i)
       adj(i) = k / 135
       k = (modulo(k, 135) * s0(i + 1)) + adj(i + 1)
    end do
    if (modulo(n, 6) < 3) then
       adj = [0, modulo(n, 6), 0, 0, 0, 0] + adj
    else
       adj = [0, modulo(n, 6), 0, 0, 0, 0] - adj
    end if
    call reduce(adj, s0, adj)

    ! apply adj to jday and msl to get the true "weekday" and solar longitude
    ! See Henning, p. 35
    if (hc .eqv. .true.) then
       jday = jday + adj
       msl = msl + adj
    else
       jday = jday - adj
       msl = msl - adj
    end if
    call normalise(jday, s0, jday)
    call reduce(msl, s0, msl)
    
  end subroutine mongolian

  subroutine bhutanese(mcount, tithi, jday)
    ! compute the time since the epoch that a given tithi begins
    ! tithi numbering begins at 0
    ! the end of tithi (N - 1) corresponds to the start of tithi N
    integer, intent(in)  :: mcount ! whole months since the epoch
    integer, intent(in)  :: tithi  ! lunar "days" since new moon
    integer, dimension(0:5), intent(out) :: jday ! time since the epoch as of the end of tithi

    ! arrays used in computing the mean weekday
    integer, dimension(0:5) :: w0
    integer, dimension(0:5) :: w1 ! synodic month
    integer, dimension(0:5) :: w2
    integer, dimension(0:5) :: w3
    !integer, dimension(0:5) :: jday ! mean weekday
    integer, dimension(0:5) :: adj ! amount to adjust by to get the semi-true weekday and true solar longitude

    ! arrays used in computing the mean solar longitude
    integer, dimension(0:5) :: s0
    integer, dimension(0:5) :: s1
    integer, dimension(0:5) :: s2
    integer, dimension(0:5) :: s3
    integer, dimension(0:5) :: msl ! mean solar longitude

    integer :: i ! counting placeholder
    integer :: k ! placeholder
    integer :: n ! placeholder

    integer, dimension(0:1) :: anomaly
    integer :: aq
    integer :: ar
    logical :: hc ! half-circle; used to note whether a half-circle is deducted from the mean solar longitude later.

    integer, dimension(0:13,0:1) :: ANOM_TABLE !Henning's Table 1-1
    integer, dimension( 0:5,0:1) :: SOLAR_TABLE !Henning's Table 1-2

    ! Henning's Table 1-1, p. 24
    ANOM_TABLE( 0,:) = [5, 0]
    ANOM_TABLE( 1,:) = [5, 5]
    ANOM_TABLE( 2,:) = [5,10]
    ANOM_TABLE( 3,:) = [5,15]
    ANOM_TABLE( 4,:) = [4,19]
    ANOM_TABLE( 5,:) = [3,22]
    ANOM_TABLE( 6,:) = [2,24]
    ANOM_TABLE( 7,:) = [1,25]
    ANOM_TABLE( 8,:) = [1,24]
    ANOM_TABLE( 9,:) = [2,22]
    ANOM_TABLE(10,:) = [3,19]
    ANOM_TABLE(11,:) = [4,15]
    ANOM_TABLE(12,:) = [5,10]
    ANOM_TABLE(13,:) = [5, 5]

    ! Henning's Table 1-2, p. 33
    SOLAR_TABLE(0,:) = [6, 0]
    SOLAR_TABLE(1,:) = [6, 6]
    SOLAR_TABLE(2,:) = [4,10]
    SOLAR_TABLE(3,:) = [1,11]
    SOLAR_TABLE(4,:) = [1,10]
    SOLAR_TABLE(5,:) = [4, 6]

    ! Compute the mean weekday
    ! This part comes from Janson, section A.3
    w0 = [      7, 60, 60, 6, 707, 707]
    w1 = [     29, 31, 50, 0, 480,   0] ! synodic month
    w2 = [2361807,  4, 24, 4, 484,   0] ! lunar epoch in Julian Days
    w3 = [      0, 59,  3, 4,  16,   0] ! length of a tithi in solar days
    jday = (mcount * w1) + w2 + (tithi * w3)
    call normalise(jday, w0, jday)

    ! Compute the anomaly
    ! Henning, p. 21
    anomaly = (mcount * [2,1]) + [3,30]
    anomaly(0) = anomaly(0) + (anomaly(1) / 126)
    anomaly(1) = modulo(anomaly(1), 126)
    anomaly(0) = modulo(anomaly(0),  28)

    ! Compute the mean solar longitude
    ! Henning, p. 22-23
    ! Janson, section A.3
    s0  = [27, 60, 60, 6, 67, 707]
    s1  = [ 2, 10, 58, 1, 17,   0] ! distance the sun travels in a synodic month, measured in nakshatras
    s2  = [ 0, 24, 10, 4, 32,   0] ! sun's zodiacal longitude at epoch, measured in nakshatras
    s3  = [ 0,  4, 21, 5, 43,   0] ! distance the sun travels in a tithi, measured in nakshatras
    msl = (mcount * s1) + s2 + (tithi * s3)
    call reduce(msl, s0, msl)

    ! Compute the semi-true weekday
    ! See Henning, p. 24-26
    aq = (anomaly(0) + tithi) / 14
    ar = modulo((anomaly(0) + tithi), 14)
    adj = 0
    n = ((anomaly(1) * 30) + tithi) * ANOM_TABLE(modulo((ar + 1), 14), 0)
    adj(1) = ANOM_TABLE(ar, 1) + (n / 3780)
    do i = 2, 4, 1
       n = modulo(n, 3780)
       n = n * w0(i)
       adj(i) = n / 3780
    end do
    call normalise(jday, w0, jday)
    if (modulo(aq, 2) == 1) then
       jday = jday - adj
    else
       jday = jday + adj
    end if

    call normalise(jday, w0, jday)

    ! adjust msl
    ! Henning, p. 31-34
    msl(0) = modulo(msl(0), 27)
    msl = msl - [6, 45, 0, 0, 0, 0]
    call reduce(msl, s0, msl)
    if ( (msl(0) > 14) .or. ( (msl(0) == 13) .and. (msl(1) >= 30) ) ) then
       hc = .true.
       msl = msl - [13, 30, 0, 0, 0, 0]
       call reduce(msl, s0, msl)
    else
       hc = .false.
    end if
    n = (msl(0) * 60) + msl(1)
    adj = [0, modulo(n, 135), msl(2), msl(3), msl(4), msl(5)]
    k = (((((adj(1) * 60) + adj(2)) * 6) + adj(3)) * 67) + adj(4) ! Henning, p. 34
    i = modulo(n, 135) + 1
    i = modulo(i, 6)
    k = k * SOLAR_TABLE(i, 1)
    adj = 0
    do i = 4, 1, (-1)
       adj(i) = modulo(k, s0(i))
       k = k / s0(i)
    end do
    k = 0
    do i = 1, 4, 1
       k = k + adj(i)
       adj(i) = k / 135
       k = (modulo(k, 135) * s0(i + 1)) + adj(i + 1)
    end do
    if (modulo(n, 6) < 3) then
       adj = [0, modulo(n, 6), 0, 0, 0, 0] + adj
    else
       adj = [0, modulo(n, 6), 0, 0, 0, 0] - adj
    end if
    call reduce(adj, s0, adj)

    ! apply adj to jday and msl to get the true "weekday" and solar longitude
    ! See Henning, p. 35
    if (hc .eqv. .true.) then
       jday = jday + adj
       msl = msl + adj
    else
       jday = jday - adj
       msl = msl - adj
    end if
    call normalise(jday, s0, jday)
    call reduce(msl, s0, msl)
    
  end subroutine bhutanese

  subroutine sherab_ling(mcount, tithi, jday)
    ! compute the time since the epoch that a given tithi begins
    ! tithi numbering begins at 0
    ! the end of tithi (N - 1) corresponds to the start of tithi N
    integer, intent(in)  :: mcount ! whole months since the epoch
    integer, intent(in)  :: tithi  ! lunar "days" since new moon
    integer, dimension(0:5), intent(out) :: jday ! time since the epoch as of the end of tithi

    ! arrays used in computing the mean weekday
    integer, dimension(0:5) :: w0
    integer, dimension(0:5) :: w1 ! synodic month
    integer, dimension(0:5) :: w2
    integer, dimension(0:5) :: w3
    !integer, dimension(0:5) :: jday ! mean weekday
    integer, dimension(0:5) :: adj ! amount to adjust by to get the semi-true weekday and true solar longitude

    ! arrays used in computing the mean solar longitude
    integer, dimension(0:5) :: s0
    integer, dimension(0:5) :: s1
    integer, dimension(0:5) :: s2
    integer, dimension(0:5) :: s3
    integer, dimension(0:5) :: msl ! mean solar longitude

    integer :: i ! counting placeholder
    integer :: k ! placeholder
    integer :: n ! placeholder

    integer, dimension(0:1) :: anomaly
    integer :: aq
    integer :: ar
    logical :: hc ! half-circle; used to note whether a half-circle is deducted from the mean solar longitude later.

    integer, dimension(0:13,0:1) :: ANOM_TABLE !Henning's Table 1-1
    integer, dimension( 0:5,0:1) :: SOLAR_TABLE !Henning's Table 1-2

    ! Henning's Table 1-1, p. 24
    ANOM_TABLE( 0,:) = [5, 0]
    ANOM_TABLE( 1,:) = [5, 5]
    ANOM_TABLE( 2,:) = [5,10]
    ANOM_TABLE( 3,:) = [5,15]
    ANOM_TABLE( 4,:) = [4,19]
    ANOM_TABLE( 5,:) = [3,22]
    ANOM_TABLE( 6,:) = [2,24]
    ANOM_TABLE( 7,:) = [1,25]
    ANOM_TABLE( 8,:) = [1,24]
    ANOM_TABLE( 9,:) = [2,22]
    ANOM_TABLE(10,:) = [3,19]
    ANOM_TABLE(11,:) = [4,15]
    ANOM_TABLE(12,:) = [5,10]
    ANOM_TABLE(13,:) = [5, 5]

    ! Henning's Table 1-2, p. 33
    SOLAR_TABLE(0,:) = [6, 0]
    SOLAR_TABLE(1,:) = [6, 6]
    SOLAR_TABLE(2,:) = [4,10]
    SOLAR_TABLE(3,:) = [1,11]
    SOLAR_TABLE(4,:) = [1,10]
    SOLAR_TABLE(5,:) = [4, 6]

    ! Compute the mean weekday
    ! This part comes from Henning, p. 18,23 and 342—346
    ! Janson, Section A.7
    
    w0 = [      7, 60, 60, 6, 707, 6811]
    w1 = [     29, 31, 50, 0, 480,    0] ! synodic month
    w2 = [2446885, 42, 47, 3, 465,    0] ! lunar epoch in Julian Days
    w3 = [      0, 59,  3, 4,  16,    0] ! length of a tithi in solar days
    jday = (mcount * w1) + w2 + (tithi * w3)
    call normalise(jday, w0, jday)

    ! Compute the anomaly
    ! Henning, p. 21
    anomaly = (mcount * [2,1]) + [19,111]
    anomaly(0) = anomaly(0) + (anomaly(1) / 126)
    anomaly(1) = modulo(anomaly(1), 126)
    anomaly(0) = modulo(anomaly(0),  28)

    ! Compute the mean solar longitude
    ! Henning, p. 22-23
    s0  = [27, 60, 60, 6, 707, 6811]
    s1  = [ 2, 10, 58, 2, 564, 5546] ! distance the sun travels in a synodic month, measured in nakshatras
    s2  = [25, 41, 58, 2,  25, 6655] ! sun's zodiacal longitude at epoch, measured in nakshatras
    s3  = [ 0,  4, 21, 5, 449, 1362] ! distance the sun travels in a tithi, measured in nakshatras
    msl = (mcount * s1) + s2 + (tithi * s3)
    call reduce(msl, s0, msl)

    ! Compute the semi-true weekday
    ! See Henning, p. 24-26
    aq = (anomaly(0) + tithi) / 14
    ar = modulo((anomaly(0) + tithi), 14)
    adj = 0
    n = ((anomaly(1) * 30) + tithi) * ANOM_TABLE(modulo((ar + 1), 14), 0)
    adj(1) = ANOM_TABLE(ar, 1) + (n / 3780)
    do i = 2, 4, 1
       n = modulo(n, 3780)
       n = n * w0(i)
       adj(i) = n / 3780
    end do
    call normalise(jday, w0, jday)
    if (modulo(aq, 2) == 1) then
       jday = jday - adj
    else
       jday = jday + adj
    end if

    ! compute the true weekday and solar longitude.
    call normalise(jday, w0, jday)

    ! adjust msl
    ! Henning, p. 31-34
    msl(0) = modulo(msl(0), 27)
    msl = msl - [6, 45, 0, 0, 0, 0]
    call reduce(msl, s0, msl)
    if ( (msl(0) > 14) .or. ( (msl(0) == 13) .and. (msl(1) >= 30) ) ) then
       hc = .true.
       msl = msl - [13, 30, 0, 0, 0, 0]
       call reduce(msl, s0, msl)
    else
       hc = .false.
    end if
    n = (msl(0) * 60) + msl(1)
    adj = [0, modulo(n, 135), msl(2), msl(3), msl(4), msl(5)]
    k = (((((adj(1) * 60) + adj(2)) * 6) + adj(3)) * 67) + adj(4) ! Henning, p. 34
    i = modulo(n, 135) + 1
    i = modulo(i, 6)
    k = k * SOLAR_TABLE(i, 1)
    adj = 0
    do i = 4, 1, (-1)
       adj(i) = modulo(k, s0(i))
       k = k / s0(i)
    end do
    k = 0
    do i = 1, 4, 1
       k = k + adj(i)
       adj(i) = k / 135
       k = (modulo(k, 135) * s0(i + 1)) + adj(i + 1)
    end do
    if (modulo(n, 6) < 3) then
       adj = [0, modulo(n, 6), 0, 0, 0, 0] + adj
    else
       adj = [0, modulo(n, 6), 0, 0, 0, 0] - adj
    end if
    call reduce(adj, s0, adj)

    ! apply adj to jday and msl to get the true "weekday" and solar longitude
    ! See Henning, p. 35
    if (hc .eqv. .true.) then
       jday = jday + adj
       msl = msl + adj
    else
       jday = jday - adj
       msl = msl - adj
    end if
    call normalise(jday, s0, jday)
    call reduce(msl, s0, msl)
    
  end subroutine sherab_ling
end module tibetan
