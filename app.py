import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ==========================================================
# 1. WEB PAGE LAYOUT & DEEP SPACE STYLING
# ==========================================================
st.set_page_config(page_title="CosmoMap Pro Engine", page_icon="🌌", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #05050a; color: #ffffff; }
    h1 { color: #00ffcc; text-shadow: 0 0 10px #00ffcc; }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 CosmoMap Pro: Graphic Mapping Engine")
st.write("Advanced boundary vector rendering interface for Class 12 Computer Science.")

if "catalog" not in st.session_state:
    st.session_state.catalog = {
        "Sagittarius A*": 4100000,
        "M87*": 6500000000,
        "Cygnus X-1": 21
    }

# ==========================================================
# 2. SIDEBAR NAVIGATION CONTROLS
# ==========================================================
st.sidebar.header("🛸 Control Panel")
option = st.sidebar.radio("Navigate Pages:", [
    "1. View Space Catalog", 
    "2. Add New Discovery", 
    "3. Map Boundaries & Graph"
])

# PAGE 1: VIEW CATALOG
if option == "1. View Space Catalog":
    st.subheader("🪐 Current Space Catalog")
    for name, mass in st.session_state.catalog.items():
        st.info(f"🌌 **{name}** — Mass: {mass:,} Solar Units")

# PAGE 2: ADD NEW DISCOVERY
elif option == "2. Add New Discovery":
    st.subheader("🚀 Catalog a New Space Object")
    new_name = st.text_input("Enter Black Hole Name:")
    new_mass = st.number_input("Enter Mass (in Solar Units):", min_value=1, value=10)
    
    if st.button("Save to Server Catalog"):
        if new_name:
            st.session_state.catalog[new_name] = new_mass
            st.success(f"✅ Success! Added '{new_name}' to the web system.")
            st.balloons()

# ==========================================================
# PAGE 3: HIGH-GRAPHICS MAPPING ENGINE
# ==========================================================
elif option == "3. Map Boundaries & Graph":
    st.subheader("📊 High-Resolution Mathematical Vector Plotting")
    
    search_name = st.selectbox("Select target black hole:", list(st.session_state.catalog.keys()))
    
    if st.button("Execute Graphic Vector Rendering"):
        mass = st.session_state.catalog[search_name]
        
        # Core Physics Calculations (Rs = 3 * Mass)
        r_s = 3 * mass
        r_p = 1.5 * r_s
        r_disk = 3.0 * r_s # Outer boundary of the searing accretion disk
        
        st.write(f"🔬 **Calculated Physical Boundaries for {search_name}:**")
        st.write(f"- 🟥 **Event Horizon (No Return Boundary):** {r_s:,} km")
        st.write(f"- 🟨 **Photon Sphere (Orbiting Light Ring):** {r_p:,} km")
        st.write(f"- 🟦 **Accretion Disk Outer Limit:** {r_disk:,} km")
        
        # --------------------------------------------------
        # SCIENTIFIC GRAPHICS PLOTTING ENGINE (MATPLOTLIB)
        # --------------------------------------------------
        # Create a deep-space dark theme plot environment
        fig, ax = plt.subplots(figsize=(6, 6), facecolor='#0a0a12')
        ax.set_facecolor('#020205')
        
        # Generate 360-degree high-density geometric angles using numpy matrices
        angles = np.linspace(0, 2 * np.pi, 500)
        
        # Compute exact circular vector coordinates for all three spaces
        x_horizon, y_horizon = r_s * np.cos(angles), r_s * np.sin(angles)
        x_photon, y_photon = r_p * np.cos(angles), r_p * np.sin(angles)
        x_disk, y_disk = r_disk * np.cos(angles), r_disk * np.sin(angles)
        
        # Layer 1: Plot the external glowing Accretion Gas Disk (Shaded Blue Core Gradient)
        ax.fill(x_disk, y_disk, color='#0044ff', alpha=0.15, label='Searing Accretion Disk')
        ax.plot(x_disk, y_disk, color='#00a2ff', linestyle=':', linewidth=1.0)
        
        # Layer 2: Plot the neon-orange Photon Sphere Orbiting Light Ring
        ax.plot(x_photon, y_photon, color='#ff9900', linestyle='--', linewidth=2.0, 
                label='Photon Sphere (Light Bound)')
        
        # Layer 3: Plot and solid-fill the pitch black gravitational Event Horizon
        ax.fill(x_horizon, y_horizon, color='#000000', edgecolor='#ff0055', linewidth=2.5, 
                label='Event Horizon (r = Rs)')
        
        # Layer 4: Plot the infinitesimal central point Singularity
        ax.plot(0, 0, marker='o', color='#ffffff', markersize=3, label='Singularity (r = 0)')
        
        # Apply strict grid line frameworks matching premium tracking software
        ax.grid(color='#1c1c3a', linestyle='-', linewidth=0.5)
        
        # Format axes, title parameters, and coordinate legends
        ax.set_title(f"Relativistic Spatial Layout: {search_name}", color='#00ffcc', fontsize=12, pad=12, weight='bold')
        ax.set_xlabel("X-Axis Spatial Displacement (km)", color='#64648c', fontsize=9)
        ax.set_ylabel("Y-Axis Spatial Displacement (km)", color='#64648c', fontsize=9)
        
        # Style coordinate ticks to match deep space display aesthetics
        ax.tick_params(colors='#64648c', labelsize=8)
        
        # Critical: Force a clean 1:1 layout scale so gravity shields don't distort into weird ellipses
        ax.set_aspect('equal', adjustable='box')
        
        # Inject standard floating legends inside the matrix layout space
        ax.legend(loc='upper right', facecolor='#0e0e1a', edgecolor='#1c1c3a', labelcolor='#ffffff', fontsize=8)
        
        # --------------------------------------------------
        # DISPLAY GRAPH ON SITE PAGE
        # --------------------------------------------------
        st.pyplot(fig)
        
        # Optional File Operation to complete file log requirements
        with open("web_space_log.txt", "a") as f:
            f.write(f"Rendered Plot for: {search_name} | Mass: {mass}\n")
        st.success("📊 Vector mesh mapping computed and logged successfully.")
