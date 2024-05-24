ROCm
====
AMD的GPU可以透過ROCm運算。AMD也把HIP（Heterogeneous Integration Platform）組態加入了ROCm，號稱可以透過HIP控制CUDA。也就是有可能透過ROCm進行container管理，就有機會橫跨AMD和NVIDIA的GPU進行運算。

## notes 20240524

手上沒有ATI GPU。從支援清單中的GPU幾乎都是MI系列。消費等級的顯卡僅看到新聞稿說有支援。目前就先測試是否能透過container中的HIP把ROCm的Tensorflow跑在NV的GPU上面。

* 安裝上，依照[quick start](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html)，到了rocm會有部分package無法安裝。如果ROCm如架構圖所說，那應該是可以直接使用Container中的版本而無須在host上安裝。因此安裝到amdgpu-dkms就直接往docker走。
* 跑docker會需要把系統的/dev/dri和/dev/kfd資料夾掛到docker裡面。這邊會有問題(如果顯卡已經驅動了，就會有/dev/dri資料夾。但/dev/kfd不一定會出現)。如果找不到/dev/kfd，可以使用[sudo modprobe amdgpu](https://golang.0voice.com/?id=4676)
* HIP在container裡面的運作，看來還沒有辦法真正跨到NV的顯卡上。後續會再拿AMD顯卡測試看看。
