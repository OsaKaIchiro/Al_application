function loadGLTF(url) {
    const canvas = document.getElementById('avatarCanvas');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true });
    renderer.setSize(canvas.clientWidth, canvas.clientHeight);

    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(5, 5, 5);
    scene.add(light);

    const loader = new THREE.GLTFLoader();
    loader.load(url, (gltf) => {
        scene.add(gltf.scene);
        camera.position.set(0, 1.5, 3);
        function animate() {
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
        }
        animate();
    }, (xhr) => {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded');
    }, (error) => {
        console.error("GLTFのロードエラー:", error);
        alert("3Dモデルのロードに失敗しました。");
    });
}

document.addEventListener("DOMContentLoaded", () => {
    loadGLTF("Creeper.glb");
});