const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')

if (toastTrigger) {
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
  toastTrigger.addEventListener('click', () => {
    toastBootstrap.show()
  })
}


// User has active
const toastRecoverTrigger = document.getElementById('liveToastRecoverBtn')
const toastRecoverLiveExample = document.getElementById('liveToastRecover')

if (toastTrigger) {
  const toastRecoverBootstrap = bootstrap.Toast.getOrCreateInstance(toastRecoverLiveExample)
  toastRecoverTrigger.addEventListener('click', () => {
    toastRecoverBootstrap.show()
  })
}