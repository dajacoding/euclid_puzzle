


!---------------------------------------------------------------
! merge ebene
function fuelleEbene(ebeneUnten, ebeneOben) result(ebeneTemp)
integer, dimension(16), intent(in) :: ebeneUnten, ebeneOben
integer, dimension(16) :: ebeneTemp
integer :: i

do i = 1,16
    ebeneTemp(i) = ebeneUnten(i)
    !if (ebene21[i] /= 0) ebeneTemp[i] = ebeneOben[i]
end do

!print *, ebeneTemp
return

end function fuelleEbene
!---------------------------------------------------------------


program euclid
!implicit none
integer,dimension(16) :: ebene1, ebene20, ebene21, ebene30, ebene31, ebene40, ebene41, ebeneTemp2, ebeneTemp3, ebeneTemp4
integer,dimension(16) :: fuelleEbene
integer :: i, j, k

ebene1  = [10,19,10,13,10, 2,15,23,19, 3, 2, 3,27,20,11,27]
ebene20 = [ 3,12,24,10, 9,22, 9, 5,10, 5, 1,24, 2,10, 9, 7]
ebene21 = [ 2, 0, 2, 0,10, 0,15, 0, 6, 0, 9, 0,16, 0,17, 0]
ebene30 = [ 5, 7, 8,24, 8, 3, 6,15,22, 6, 1, 1,11,27,14, 5]
ebene31 = [10, 0, 2, 0,22, 0, 2, 0,17, 0,15, 0,14, 0, 5, 0]
ebene40 = [ 1, 6,10, 6,10, 2, 6,10, 4, 1, 5, 5, 4, 8, 6, 3]
ebene41 = [10, 0,10, 0,10, 0, 6, 0,13, 0, 3, 0, 3, 0, 6, 0]

ebeneTemp2 = fuelleEbene(ebene20, ebene21)


end 


!---------------------------------------------------------------



!do i=1,13
!do j=i,13
!do k=j,13
!do l=k,13
!x(1)=i
!x(2)=j
!x(3)=k
!x(4)=l
!if(XXIV(x)==1)print"(4(i0,a1))",i,"",j,"",k,"",l,""
!end do
!end do 
!end do
!end do
!end
!
!integer function XXIV(x)
!integer::t,i
!integer,dimension(4)::x
!do i=1,4
!t=t+x(i)
!end do
!XXIV=0
!if(t==24) XXIV=1
!return
!end function XXIV
