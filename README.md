# 🚀 Data Mesh Architecture on Microsoft Fabric

**Multi-Domain Data Mesh | Real-Time Analytics | OneLake Shortcuts | KQL Database**

[![Microsoft Fabric](https://img.shields.io/badge/Microsoft_Fabric-F34F21?logo=microsoft)](https://fabric.microsoft.com/)
[![KQL](https://img.shields.io/badge/KQL-0078D4?logo=kusto)](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?logo=powerbi)](https://powerbi.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Overview

Enterprise-scale **Data Mesh** implementation on Microsoft Fabric unifying three disparate business domains (Transactions, Logistics, Governance) into a single semantic model. Demonstrates hybrid batch + near real-time analytics without data duplication using OneLake Shortcuts and KQL Database.

This project showcases modern data architecture patterns for organizations managing complex multi-domain data landscapes with varying latency requirements.

---

## 💼 Business Impact

- **Unified Analytics**: Single semantic model combining batch + real-time data sources
- **Zero-Copy Architecture**: OneLake Shortcuts eliminate data duplication
- **SLA Compliance Tracking**: Real-time monitoring of delivery performance across carriers
- **Cross-Domain Insights**: Correlate system failures (Governance) with sales impact (Transactions)

---

## 🛠️ Technical Stack

| Category | Technologies |
| :--- | :--- |
| **Platform** | Microsoft Fabric |
| **Data Engineering** | PySpark, Dataflows Gen2 |
| **Real-Time Ingestion** | KQL Database (Eventhouse) |
| **Data Storage** | OneLake, Delta Lake |
| **Data Virtualization** | OneLake Shortcuts |
| **BI & Analytics** | Power BI, DAX |
| **Query Language** | KQL, SQL, DAX |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA MESH ARCHITECTURE                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  DOMAIN 1: TRANSACTIONS (D1)                                │
│  └─→ Lakehouse (Delta Lake)                                 │
│      Sales records, revenue data (Batch)                    │
│                                                              │
│  DOMAIN 2: LOGISTICS (D2)                                   │
│  └─→ KQL Database (Eventhouse)                              │
│      Carrier status, delivery times (Near Real-Time)        │
│                                                              │
│  DOMAIN 3: GOVERNANCE (D3)                                  │
│  └─→ KQL Database (Eventhouse)                              │
│      System logs, SLA compliance (Near Real-Time)           │
│                                                              │
│  CONSUMPTION LAYER (D4)                                     │
│  └─→ Lakehouse with OneLake Shortcuts → D2, D3              │
│      Zero-copy data access, unified semantic model          │
│                                                              │
│  SEMANTIC MODEL                                             │
│  └─→ Power BI Dataset with DAX measures                     │
│      Cross-domain relationships, KPIs                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Key Features

### Multi-Domain Integration
| Domain | Content | Data Latency | Technology |
| :--- | :--- | :--- | :--- |
| **D1: Transactions** | Sales & Revenue Records | Batch | Lakehouse (Delta Lake) |
| **D2: Logistics** | Carrier Status, Delivery Times | Near Real-Time | KQL Database |
| **D3: Governance** | System Logs, SLA Compliance | Near Real-Time | KQL Database |

### Zero-Copy Data Access
- **OneLake Shortcuts**: Point directly to KQL data without copying
- **Real-Time Sync**: Analytics always reflect latest operational data
- **Cost Optimization**: No storage duplication across domains

### DAX Measures & KPIs
- `[Tiempo Promedio Entrega (días)]`: Average delivery time
- `[Tasa Incumbimiento SLA]`: SLA violation rate
- `[Total Envíos]`: Total shipments count

---

## 📊 Results & Metrics

| Metric | Value |
| :--- | :--- |
| **Domains Unified** | 3 (Transactions, Logistics, Governance) |
| **Data Latency** | Batch + Near Real-Time (KQL) |
| **Storage Efficiency** | Zero-copy via OneLake Shortcuts |
| **Dashboard Pages** | Multi-page with cross-domain filters |

---

## 📁 Project Structure

```
DataMesh_Fabric_Logistics/
├── 01_Architecture_and_Ingestion/    # Ingestion scripts & documentation
├── 02_Data_Modeling_and_DAX/         # Data model & DAX measures
├── Gobernanza de Datos/              # Governance documentation
├── Dashboard Logística en DataMesh.pbix  # Power BI report
├── Resumen Ejecutivo del Proyecto Data Mesh en Microsoft Fabric.pdf
├── dashboard datamesh_foto.png       # Dashboard screenshot
└── README.md                          # Project documentation
```

---

## 🔧 Setup & Installation

### Prerequisites
- Microsoft Fabric capacity (F64 or higher recommended)
- Power BI Desktop (latest version)
- Appropriate Fabric workspace permissions

### Deployment Steps

```bash
# Clone the repository
git clone https://github.com/Nicolenki7/DataMesh_Fabric_Logistics.git
cd DataMesh_Fabric_Logistics

# 1. Create Fabric Workspace
# 2. Create Lakehouse for Transactions (D1)
# 3. Create KQL Database for Logistics (D2) and Governance (D3)
# 4. Set up OneLake Shortcuts in consumption Lakehouse (D4)
# 5. Import Power BI report (Dashboard Logística en DataMesh.pbix)
# 6. Configure DAX measures and relationships
```

### Configuration

1. **Ingest Transaction Data**: Upload to Lakehouse (D1)
2. **Configure KQL Ingestion**: Set up Eventhouse for D2, D3
3. **Create Shortcuts**: Point D4 Lakehouse to KQL tables
4. **Build Semantic Model**: Define relationships in Power BI
5. **Deploy Dashboard**: Publish to Fabric workspace

---

## 📈 Usage

### Dashboard Navigation

| Visualization | Domains Integrated | Business Value |
| :--- | :--- | :--- |
| **Sales Map** | D1 + D2 | Inventory strategy by delivery region |
| **SLA Audit** | D1 + D3 | Tech risk: system failures vs payment methods |
| **Carrier Performance** | D2 | Cost/efficiency audit (fastest carrier) |
| **Historical Trend** | D2 | Planning: delivery efficiency over time |

### Interactive Filters
- **Carrier Selector**: Filter entire analysis by logistics operator
- **Date Range**: Adjust time window for trend analysis
- **Region Filter**: Focus on specific delivery zones

---

## 🎯 Key Learnings

- **OneLake Shortcuts** enable zero-copy real-time analytics
- **KQL Database** handles high-velocity ingestion efficiently
- **Cross-domain relationships** unlock insights impossible in siloed architectures
- **DAX optimization** critical for hybrid batch/real-time models

---

## 🖼️ Dashboard Screenshot

![Data Mesh Dashboard](https://github.com/Nicolenki7/DataMesh_Fabric_Logistics/blob/main/dashboard%20datamesh_foto.png)

---

## 🔮 Future Enhancements

- [ ] Additional domain integration (Customer, Product)
- [ ] Real-time alerting for SLA violations
- [ ] Predictive delivery time estimation (ML)
- [ ] Carrier cost optimization recommendations
- [ ] Automated data quality monitoring

---

## 🔗 Links

| Resource | URL |
| :--- | :--- |
| **Repository** | https://github.com/Nicolenki7/DataMesh_Fabric_Logistics |
| **Live Dashboard** | [View in Fabric](https://app.fabric.microsoft.com/reportEmbed?reportId=75459c29-c7dd-404b-b4e2-f4a256e3a6a8) |

---

## 📝 Resumen en Español

Este proyecto demuestra la implementación exitosa de una arquitectura **Data Mesh** en **Microsoft Fabric** para resolver la fragmentación de datos de una compañía con múltiples operadores logísticos (DHL, FedEx, UPS, LocalPost).

Se unificaron tres dominios (Transacciones, Logística, Gobernanza) en un único **Modelo Semántico** usando **OneLake Shortcuts** para acceso zero-copy a datos en tiempo real. El dashboard final permite análisis híbrido de datos de lote y near real-time con medidas DAX para auditoría de SLA y rendimiento de operadores.

---

## 📄 License

MIT License — Feel free to fork, modify, and use for personal or commercial projects.

---

## 👤 Author

**Nicolás Zalazar** | Senior Data Engineer & Microsoft Fabric Specialist

- GitHub: [@Nicolenki7](https://github.com/Nicolenki7)
- LinkedIn: [nicolas-zalazar-63340923a](https://www.linkedin.com/in/nicolas-zalazar-63340923a)
- Portfolio: [nicolenki7.github.io/Portfolio](https://nicolenki7.github.io/Portfolio/)
- Email: zalazarn046@gmail.com

---

*Last Updated: March 2026*
