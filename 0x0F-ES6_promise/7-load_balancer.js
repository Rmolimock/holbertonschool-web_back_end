export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]).then((mess) => mess);
}
