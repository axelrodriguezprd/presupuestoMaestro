from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':

        # 1 Presupuesto de ventas
        PApresVenUnidVend1S = request.form['PApresVenUnidVend1S']
        PApresVenPrecVent1S = request.form['PApresVenPrecVent1S']
        PApresVenUnidVend2S = request.form['PApresVenUnidVend2S']
        PApresVenPrecVent2S = request.form['PApresVenPrecVent2S']

        PBpresVenUnidVend1S = request.form['PBpresVenUnidVend1S']
        PBpresVenPrecVent1S = request.form['PBpresVenPrecVent1S']
        PBpresVenUnidVend2S = request.form['PBpresVenUnidVend2S']
        PBpresVenPrecVent2S = request.form['PBpresVenPrecVent2S']

        PCpresVenUnidVend1S = request.form['PCpresVenUnidVend1S']
        PCpresVenPrecVent1S = request.form['PCpresVenPrecVent1S']
        PCpresVenUnidVend2S = request.form['PCpresVenUnidVend2S']
        PCpresVenPrecVent2S = request.form['PCpresVenPrecVent2S']

        PAIV1S = float(PApresVenUnidVend1S) * float(PApresVenPrecVent1S)
        PAIV2S = float(PApresVenUnidVend2S) * float(PApresVenPrecVent2S)
        TotalAnualPA = PAIV1S + PAIV2S

        PBIV1S = float(PBpresVenUnidVend1S) * float(PBpresVenPrecVent1S)
        PBIV2S = float(PBpresVenUnidVend2S) * float(PBpresVenPrecVent2S)
        TotalAnualPB = PBIV1S + PBIV2S

        PCIV1S = float(PCpresVenUnidVend1S) * float(PCpresVenPrecVent1S)
        PCIV2S = float(PCpresVenUnidVend2S) * float(PCpresVenPrecVent2S)
        TotalAnualPC = PCIV1S + PCIV2S

        TotalVentasPorSemestre = TotalAnualPA + TotalAnualPB + TotalAnualPC

        # 2 Determinacion del saldo de Clientes y Flujo de Entradas

        DSCFESaldo2020 = request.form['DSCFESaldo2020']
        DSCFEPorcentaje2020 = request.form['DSCFEPorcentaje2020']
        DSCFEPorcentaje2021 = request.form['DSCFEPorcentaje2021']

        DSCFETotal2021 = TotalVentasPorSemestre + float(DSCFESaldo2020)
        DSCFECobranza2020 = float(DSCFESaldo2020) * float(float(DSCFEPorcentaje2020) / 100)
        DSCFECobranza2021 = TotalVentasPorSemestre * float(float(DSCFEPorcentaje2021) / 100)
        DSCFETotalEnt2021 = DSCFECobranza2020 + DSCFECobranza2021
        DSCFESaldoClientes2021 = DSCFETotal2021 - DSCFETotalEnt2021

        # 3 Presupuesto de produccion

        #Producto A
        PAPPInvFinal1S = request.form['PAPPInvFinal1S']
        PAPPInvFinal2S = request.form['PAPPInvFinal2S']
        PAPPInvInicial1S = request.form['PAPPInvInicial1S']

        PAPPPApresVenUnidVend1S = int(PApresVenUnidVend1S)
        PAPPPApresVenUnidVend2S = int(PApresVenUnidVend2S)
        PAPPUnidsAVender = int(PApresVenUnidVend1S) + int(PApresVenUnidVend2S)
        PAPPInvFinalTotal2021 = PAPPPApresVenUnidVend2S
        PAPPTotalUnidades1S = PAPPUnidsAVender + int(PAPPInvFinal1S)
        PAPPTotalUnidades2S = PAPPPApresVenUnidVend2S + int(PAPPInvFinal2S)
        PAPPTotalUnidades2021 = PAPPUnidsAVender + PAPPInvFinalTotal2021
        PAPPInvInicial2S = int(PAPPInvFinal1S)
        PAPPInvTotal2021 = int(PAPPInvInicial1S)
        PAPPUnidsAProducir1S = PAPPTotalUnidades1S - int(PAPPInvInicial1S)
        PAPPUnidsAProducir2S = PAPPTotalUnidades2S - int(PAPPInvInicial2S)
        PAPPUnidsAProducir2021 = PAPPTotalUnidades2021 - int(PAPPInvTotal2021)

        #Producto B    
        PBPPInvFinal1S = request.form['PBPPInvFinal1S']
        PBPPInvFinal2S = request.form['PBPPInvFinal2S']
        PBPPInvInicial1S = request.form['PBPPInvInicial1S']

        PBPPPApresVenUnidVend1S = int(PBpresVenUnidVend1S)
        PBPPPApresVenUnidVend2S = int(PBpresVenUnidVend2S)
        PBPPUnidsAVender = int(PBpresVenUnidVend1S) + int(PBpresVenUnidVend2S)
        PBPPInvFinalTotal2021 = PBPPPApresVenUnidVend2S
        PBPPTotalUnidades1S = PBPPUnidsAVender + int(PBPPInvFinal1S)
        PBPPTotalUnidades2S = PBPPPApresVenUnidVend2S + int(PBPPInvFinal2S)
        PBPPTotalUnidades2021 = PBPPUnidsAVender + PBPPInvFinalTotal2021
        PBPPInvInicial2S = int(PBPPInvFinal1S)
        PBPPInvTotal2021 = int(PBPPInvInicial1S)
        PBPPUnidsAProducir1S = PBPPTotalUnidades1S - int(PBPPInvInicial1S)
        PBPPUnidsAProducir2S = PBPPTotalUnidades2S - int(PBPPInvInicial2S)
        PBPPUnidsAProducir2021 = PBPPTotalUnidades2021 - int(PBPPInvTotal2021)

        #Producto C
        PCPPInvFinal1S = request.form['PCPPInvFinal1S']
        PCPPInvFinal2S = request.form['PCPPInvFinal2S']
        PCPPInvInicial1S = request.form['PCPPInvInicial1S']

        PCPPPApresVenUnidVend1S = int(PCpresVenUnidVend1S)
        PCPPPApresVenUnidVend2S = int(PCpresVenUnidVend2S)
        PCPPUnidsAVender = int(PCpresVenUnidVend1S) + int(PCpresVenUnidVend2S)
        PCPPInvFinalTotal2021 = PCPPPApresVenUnidVend2S
        PCPPTotalUnidades1S = PCPPUnidsAVender + int(PCPPInvFinal1S)
        PCPPTotalUnidades2S = PCPPPApresVenUnidVend2S + int(PCPPInvFinal2S)
        PCPPTotalUnidades2021 = PCPPUnidsAVender + PCPPInvFinalTotal2021
        PCPPInvInicial2S = int(PCPPInvFinal1S)
        PCPPInvTotal2021 = int(PCPPInvInicial1S)
        PCPPUnidsAProducir1S = PCPPTotalUnidades1S - int(PCPPInvInicial1S)
        PCPPUnidsAProducir2S = PCPPTotalUnidades2S - int(PCPPInvInicial2S)
        PCPPUnidsAProducir2021 = PCPPTotalUnidades2021 - int(PCPPInvTotal2021)

        # 4. Presupuesto de Requerimiento de Materiales

        #Producto A
        #Material A
        PAPRMReqMatA = request.form['PAPRMReqMatA']

        PAPRMTotalMatA1S = PAPPUnidsAProducir1S * int(PAPRMReqMatA)
        PAPRMTotalMatA2S = PAPPUnidsAProducir2S * int(PAPRMReqMatA)
        PAPRMTotalMatATotal = PAPPUnidsAProducir2021 * int(PAPRMReqMatA)
        
        #Material B
        PAPRMReqMatB = request.form['PAPRMReqMatB']

        PAPRMTotalMatB1S = PAPPUnidsAProducir1S * int(PAPRMReqMatB)
        PAPRMTotalMatB2S = PAPPUnidsAProducir2S * int(PAPRMReqMatB)
        PAPRMTotalMatBTotal = PAPPUnidsAProducir2021 * int(PAPRMReqMatB)

        #Material B
        PAPRMReqMatC = request.form['PAPRMReqMatC']

        PAPRMTotalMatC1S = PAPPUnidsAProducir1S * int(PAPRMReqMatC)
        PAPRMTotalMatC2S = PAPPUnidsAProducir2S * int(PAPRMReqMatC)
        PAPRMTotalMatCTotal = PAPPUnidsAProducir2021 * int(PAPRMReqMatC)

        #Producto B
        #Material A
        PBPRMReqMatA = request.form['PBPRMReqMatA']

        PBPRMTotalMatA1S = PBPPUnidsAProducir1S * int(PBPRMReqMatA)
        PBPRMTotalMatA2S = PBPPUnidsAProducir2S * int(PBPRMReqMatA)
        PBPRMTotalMatATotal = PBPPUnidsAProducir2021 * int(PBPRMReqMatA)
        
        #Material B
        PBPRMReqMatB = request.form['PBPRMReqMatB']

        PBPRMTotalMatB1S = PBPPUnidsAProducir1S * int(PBPRMReqMatB)
        PBPRMTotalMatB2S = PBPPUnidsAProducir2S * int(PBPRMReqMatB)
        PBPRMTotalMatBTotal = PBPPUnidsAProducir2021 * int(PBPRMReqMatB)

        #Material B
        PBPRMReqMatC = request.form['PBPRMReqMatC']

        PBPRMTotalMatC1S = PBPPUnidsAProducir1S * int(PBPRMReqMatC)
        PBPRMTotalMatC2S = PBPPUnidsAProducir2S * int(PBPRMReqMatC)
        PBPRMTotalMatCTotal = PBPPUnidsAProducir2021 * int(PBPRMReqMatC)

        #Producto C
        #Material A
        PCPRMReqMatA = request.form['PCPRMReqMatA']

        PCPRMTotalMatA1S = PCPPUnidsAProducir1S * int(PCPRMReqMatA)
        PCPRMTotalMatA2S = PCPPUnidsAProducir2S * int(PCPRMReqMatA)
        PCPRMTotalMatATotal = PCPPUnidsAProducir2021 * int(PCPRMReqMatA)
        
        #Material B
        PCPRMReqMatB = request.form['PCPRMReqMatB']

        PCPRMTotalMatB1S = PCPPUnidsAProducir1S * int(PCPRMReqMatB)
        PCPRMTotalMatB2S = PCPPUnidsAProducir2S * int(PCPRMReqMatB)
        PCPRMTotalMatBTotal = PCPPUnidsAProducir2021 * int(PCPRMReqMatB)

        #Material B
        PCPRMReqMatC = request.form['PCPRMReqMatC']

        PCPRMTotalMatC1S = PCPPUnidsAProducir1S * int(PCPRMReqMatC)
        PCPRMTotalMatC2S = PCPPUnidsAProducir2S * int(PCPRMReqMatC)
        PCPRMTotalMatCTotal = PCPPUnidsAProducir2021 * int(PCPRMReqMatC)

        #Total De Requerimientos 
        #Material A
        #1er Semestre
        TotalMatAReqPP1S = PAPRMTotalMatA1S + PBPRMTotalMatA1S + PCPRMTotalMatA1S
        #2do Semestre
        TotalMatAReqPP2S = PAPRMTotalMatA2S + PAPRMTotalMatA2S + PAPRMTotalMatA2S
        #Total 2021
        TotalPARPMMatA = PAPRMTotalMatATotal + PBPRMTotalMatATotal + PCPRMTotalMatATotal

        #Material B
        #1er Semestre
        TotalMatBReqPP1S = PAPRMTotalMatB1S + PBPRMTotalMatB1S + PCPRMTotalMatB1S
        #2do Semestre
        TotalMatBReqPP2S = PAPRMTotalMatB2S + PBPRMTotalMatB2S + PCPRMTotalMatB2S
        #Total 2021
        TotalPARPMMatB = PAPRMTotalMatBTotal + PBPRMTotalMatBTotal + PCPRMTotalMatBTotal

        #Material C
        #1er Semestre
        TotalMatCReqPP1S = PAPRMTotalMatC1S + PBPRMTotalMatC1S + PCPRMTotalMatC1S
        #2do Semestre
        TotalMatCReqPP2S = PAPRMTotalMatC2S + PBPRMTotalMatC2S + PCPRMTotalMatC2S
        #Total 2021
        TotalPARPMMatC = PAPRMTotalMatCTotal + PBPRMTotalMatCTotal + PCPRMTotalMatCTotal

        # 5. Presupuesto de Compra de Materiales
        #Material A
        MAPCMInvFinal1S = request.form['MAPCMInvFinal1S']
        MAPCMInvFinal2S = request.form['MAPCMInvFinal2S']
        MAPCMPrecioComp1S = request.form['MAPCMPrecioComp1S']
        MAPCMPrecioComp2S = request.form['MAPCMPrecioComp2S']

        MAPCMTotalMat1S = TotalMatAReqPP1S + int(MAPCMInvFinal1S)
        MAPCMTotalMat2S = TotalMatAReqPP2S + int(MAPCMInvFinal2S)
        MAPCMTotalMatAnual = TotalPARPMMatA + int(MAPCMInvFinal2S)
        MAPCMMatComp1S = MAPCMTotalMat1S - int(MAPCMInvFinal1S)
        MAPCMMatComp2S = MAPCMTotalMat2S - int(MAPCMInvFinal1S)
        MAPCMMatCompAnual = MAPCMTotalMatAnual - int(MAPCMInvFinal1S)
        MAPCMTotalEnPesos1S = MAPCMMatComp1S * int(MAPCMPrecioComp1S)
        MAPCMTotalEnPesos2S = MAPCMMatComp2S * int(MAPCMPrecioComp2S)
        MAPCMTotalEnPesosAnual = MAPCMTotalEnPesos1S + MAPCMTotalEnPesos2S

        #Material B
        MBPCMInvFinal1S = request.form['MBPCMInvFinal1S']
        MBPCMInvFinal2S = request.form['MBPCMInvFinal2S']
        MBPCMPrecioComp1S = request.form['MBPCMPrecioComp1S']
        MBPCMPrecioComp2S = request.form['MBPCMPrecioComp2S']

        MBPCMTotalMat1S = TotalMatBReqPP1S + int(MBPCMInvFinal1S)
        MBPCMTotalMat2S = TotalMatBReqPP2S + int(MBPCMInvFinal2S)
        MBPCMTotalMatAnual = TotalPARPMMatB + int(MBPCMInvFinal2S)
        MBPCMMatComp1S = MBPCMTotalMat1S - int(MBPCMInvFinal1S)
        MBPCMMatComp2S = MBPCMTotalMat2S - int(MBPCMInvFinal1S)
        MBPCMMatCompAnual = MBPCMTotalMatAnual - int(MBPCMInvFinal1S)
        MBPCMTotalEnPesos1S = MBPCMMatComp1S * int(MBPCMPrecioComp1S)
        MBPCMTotalEnPesos2S = MBPCMMatComp2S * int(MBPCMPrecioComp2S)
        MBPCMTotalEnPesosAnual = MBPCMTotalEnPesos1S + MBPCMTotalEnPesos2S

        #Material C
        MCPCMInvFinal1S = request.form['MCPCMInvFinal1S']
        MCPCMInvFinal2S = request.form['MCPCMInvFinal2S']
        MCPCMPrecioComp1S = request.form['MCPCMPrecioComp1S']
        MCPCMPrecioComp2S = request.form['MCPCMPrecioComp2S']

        MCPCMTotalMat1S = TotalMatCReqPP1S + int(MCPCMInvFinal1S)
        MCPCMTotalMat2S = TotalMatCReqPP2S + int(MCPCMInvFinal2S)
        MCPCMTotalMatAnual = TotalPARPMMatC + int(MCPCMInvFinal2S)
        MCPCMMatComp1S = MCPCMTotalMat1S - int(MCPCMInvFinal1S)
        MCPCMMatComp2S = MCPCMTotalMat2S - int(MCPCMInvFinal1S)
        MCPCMMatCompAnual = MCPCMTotalMatAnual - int(MCPCMInvFinal1S)
        MCPCMTotalEnPesos1S = MCPCMMatComp1S * int(MCPCMPrecioComp1S)
        MCPCMTotalEnPesos2S = MBPCMMatComp2S * int(MCPCMPrecioComp2S)
        MCPCMTotalEnPesosAnual = MCPCMTotalEnPesos1S + MCPCMTotalEnPesos2S

        #Total de compras de materiales
        TMPCM1S = MAPCMTotalEnPesos1S + MBPCMTotalEnPesos1S + MCPCMTotalEnPesos1S
        TMPCM2S = MAPCMTotalEnPesos2S + MBPCMTotalEnPesos2S + MCPCMTotalEnPesos2S
        TMPCMAnual = MAPCMTotalEnPesosAnual + MBPCMTotalEnPesosAnual + MCPCMTotalEnPesosAnual

        # 6. Determinación del saldo de Proveedores y Flujo de Salidas

        DSPFSSaldoProvTotal2020 = request.form['DSPFSSaldoProvTotal2020']
        DSPFSPorceProv2020 = request.form['DSPFSPorceProv2020']
        DSPFSPorceProv2021 = request.form['DSPFSPorceProv2021']

        DSPFSTotalProv2021 = float(DSPFSSaldoProvTotal2020) + float(TMPCMAnual)
        DSPFSPorProv2020 =   float(DSPFSSaldoProvTotal2020) * float((float(DSPFSPorceProv2020) / 100))
        DSPFSPorProv2021 =   float(TMPCMAnual) * float((float(DSPFSPorceProv2021) / 100))
        DSPFSTotalSalidas2021 = DSPFSPorProv2020 + DSPFSPorProv2021
        DSPFSSaldoTotal2021 = DSPFSTotalProv2021 + DSPFSTotalSalidas2021

        # 7. Presupuesto de Mano de Obra Directa

        #Producto A
        PAPMODHorasReq = request.form['PAPMODHorasReq']
        PAPMODCuotaHora1S = request.form['PAPMODCuotaHora1S']
        PAPMODCuotaHora2S = request.form['PAPMODCuotaHora2S']


        PAPMODTotalHorasRequer1S = PAPPUnidsAProducir1S * int(PAPMODHorasReq)
        PAPMODTotalHorasRequer2S = PAPPUnidsAProducir2S * int(PAPMODHorasReq)
        PAPMODTotalHorasRequerAnual = PAPPUnidsAProducir2021 * int(PAPMODHorasReq)
        PAMODImporte1S = float(PAPMODTotalHorasRequer1S) * float(PAPMODCuotaHora1S)
        PAMODImporte2S = float(PAPMODTotalHorasRequer2S) * float(PAPMODCuotaHora2S)
        PAMODImporteAnual = PAMODImporte1S + PAMODImporte2S

        #Producto B 
        PBPMODHorasReq = request.form['PBPMODHorasReq']
        PBPMODCuotaHora1S = request.form['PBPMODCuotaHora1S']
        PBPMODCuotaHora2S = request.form['PBPMODCuotaHora2S']


        PBPMODTotalHorasRequer1S = PBPPUnidsAProducir1S * int(PBPMODHorasReq)
        PBPMODTotalHorasRequer2S = PBPPUnidsAProducir2S * int(PBPMODHorasReq)
        PBPMODTotalHorasRequerAnual = PBPPUnidsAProducir2021 * int(PBPMODHorasReq)
        PBMODImporte1S = float(PBPMODTotalHorasRequer1S) * float(PBPMODCuotaHora1S)
        PBMODImporte2S = float(PBPMODTotalHorasRequer2S) * float(PBPMODCuotaHora2S)
        PBMODImporteAnual = PBMODImporte1S + PBMODImporte2S

        #Producto C
        PCPMODHorasReq = request.form['PCPMODHorasReq']
        PCPMODCuotaHora1S = request.form['PCPMODCuotaHora1S']
        PCPMODCuotaHora2S = request.form['PCPMODCuotaHora2S']


        PCPMODTotalHorasRequer1S = PCPPUnidsAProducir1S * int(PCPMODHorasReq)
        PCPMODTotalHorasRequer2S = PCPPUnidsAProducir2S * int(PCPMODHorasReq)
        PCPMODTotalHorasRequerAnual = PCPPUnidsAProducir2021 * int(PCPMODHorasReq)
        PCMODImporte1S = float(PCPMODTotalHorasRequer1S) * float(PCPMODCuotaHora1S)
        PCMODImporte2S = float(PCPMODTotalHorasRequer2S) * float(PCPMODCuotaHora2S)
        PCMODImporteAnual = PCMODImporte1S + PCMODImporte2S

        #Totales
        PMODTotalHoras1S = PAPMODTotalHorasRequer1S + PBPPUnidsAProducir1S + PCPMODTotalHorasRequer1S
        PMODTotalHoras2S = PAPMODTotalHorasRequer2S + PBPPUnidsAProducir2S + PCPMODTotalHorasRequer2S
        PMODTotalHorasAnual = PAPMODTotalHorasRequerAnual + PBPMODTotalHorasRequerAnual + PCPMODTotalHorasRequerAnual

        PMODTotalMOD1S = PAMODImporte1S + PBMODImporte1S + PCMODImporte1S
        PMODTotalMOD2S = PAMODImporte2S + PBMODImporte2S + PCMODImporte2S
        PMODTotalMODAnual = PAMODImporteAnual + PBMODImporteAnual + PCMODImporteAnual


        return render_template(
            'app.html',
            PAIV1S=PAIV1S,
            PAIV2S=PAIV2S,
            TotalAnualPA=TotalAnualPA,
            PBIV1S=PBIV1S, 
            PBIV2S=PBIV2S,
            TotalAnualPB=TotalAnualPB, 
            PCIV1S=PCIV1S,
            PCIV2S=PCIV2S, TotalAnualPC=TotalAnualPC,
            TotalVentasPorSemestre=TotalVentasPorSemestre,
            DSCFESaldo2020=DSCFESaldo2020,
            DSCFETotal2021=DSCFETotal2021,
            DSCFECobranza2020=DSCFECobranza2020,
            DSCFECobranza2021=DSCFECobranza2021,
            DSCFETotalEnt2021=DSCFETotalEnt2021,
            DSCFESaldoClientes2021=DSCFESaldoClientes2021,
            PAPPUnidsAVender=PAPPUnidsAVender,
            PAPPPApresVenUnidVend1S=PAPPPApresVenUnidVend1S,
            PAPPPApresVenUnidVend2S=PAPPPApresVenUnidVend2S,
            PAPPInvFinalTotal2021=PAPPInvFinalTotal2021,
            PAPPTotalUnidades1S=PAPPTotalUnidades1S,
            PAPPTotalUnidades2S=PAPPTotalUnidades2S,
            PAPPTotalUnidades2021=PAPPTotalUnidades2021,
            PAPPInvInicial2S=PAPPInvInicial2S,
            PAPPInvTotal2021=PAPPInvTotal2021,
            PAPPUnidsAProducir1S = PAPPUnidsAProducir1S,
            PAPPUnidsAProducir2S = PAPPUnidsAProducir2S,
            PAPPUnidsAProducir2021 = PAPPUnidsAProducir2021,
            PBPPUnidsAVender=PBPPUnidsAVender,
            PBPPPApresVenUnidVend1S=PBPPPApresVenUnidVend1S,
            PBPPPApresVenUnidVend2S=PBPPPApresVenUnidVend2S,
            PBPPInvFinalTotal2021=PBPPInvFinalTotal2021,
            PBPPTotalUnidades1S=PBPPTotalUnidades1S,
            PBPPTotalUnidades2S=PBPPTotalUnidades2S,
            PBPPTotalUnidades2021=PBPPTotalUnidades2021,
            PBPPInvInicial2S=PBPPInvInicial2S,
            PBPPInvTotal2021=PBPPInvTotal2021,
            PBPPUnidsAProducir1S = PBPPUnidsAProducir1S,
            PBPPUnidsAProducir2S = PBPPUnidsAProducir2S,
            PBPPUnidsAProducir2021 = PBPPUnidsAProducir2021,
            PCPPUnidsAVender=PCPPUnidsAVender,
            PCPPPApresVenUnidVend1S=PCPPPApresVenUnidVend1S,
            PCPPPApresVenUnidVend2S=PCPPPApresVenUnidVend2S,
            PCPPInvFinalTotal2021=PCPPInvFinalTotal2021,
            PCPPTotalUnidades1S=PCPPTotalUnidades1S,
            PCPPTotalUnidades2S=PCPPTotalUnidades2S,
            PCPPTotalUnidades2021=PCPPTotalUnidades2021,
            PCPPInvInicial2S=PCPPInvInicial2S,
            PCPPInvTotal2021=PCPPInvTotal2021,
            PCPPUnidsAProducir1S = PCPPUnidsAProducir1S,
            PCPPUnidsAProducir2S = PCPPUnidsAProducir2S,
            PCPPUnidsAProducir2021 = PCPPUnidsAProducir2021,
            PAPRMReqMatA = PAPRMReqMatA,
            PAPRMTotalMatA1S = PAPRMTotalMatA1S,
            PAPRMTotalMatA2S = PAPRMTotalMatA2S,
            PAPRMTotalMatATotal = PAPRMTotalMatATotal,
            PAPRMTotalMatB1S = PAPRMTotalMatB1S,
            PAPRMTotalMatB2S = PAPRMTotalMatB2S,
            PAPRMTotalMatBTotal = PAPRMTotalMatBTotal,
            PAPRMTotalMatC1S = PAPRMTotalMatC1S,
            PAPRMTotalMatC2S = PAPRMTotalMatC2S,
            PAPRMTotalMatCTotal = PAPRMTotalMatCTotal,
            PBPRMReqMatA = PBPRMReqMatA,
            PBPRMTotalMatA1S = PBPRMTotalMatA1S,
            PBPRMTotalMatA2S = PBPRMTotalMatA2S,
            PBPRMTotalMatATotal = PBPRMTotalMatATotal,
            PBPRMTotalMatB1S = PBPRMTotalMatB1S,
            PBPRMTotalMatB2S = PBPRMTotalMatB2S,
            PBPRMTotalMatBTotal = PBPRMTotalMatBTotal,
            PBPRMTotalMatC1S = PBPRMTotalMatC1S,
            PBPRMTotalMatC2S = PBPRMTotalMatC2S,
            PBPRMTotalMatCTotal = PBPRMTotalMatCTotal,
            PCPRMReqMatA = PCPRMReqMatA,
            PCPRMTotalMatA1S = PCPRMTotalMatA1S,
            PCPRMTotalMatA2S = PCPRMTotalMatA2S,
            PCPRMTotalMatATotal = PCPRMTotalMatATotal,
            PCPRMTotalMatB1S = PCPRMTotalMatB1S,
            PCPRMTotalMatB2S = PCPRMTotalMatB2S,
            PCPRMTotalMatBTotal = PCPRMTotalMatBTotal,
            PCPRMTotalMatC1S = PCPRMTotalMatC1S,
            PCPRMTotalMatC2S = PCPRMTotalMatC2S,
            PCPRMTotalMatCTotal = PCPRMTotalMatCTotal,
            TotalMatAReqPP1S = TotalMatAReqPP1S,
            TotalMatAReqPP2S = TotalMatAReqPP2S,
            TotalPARPMMatA = TotalPARPMMatA,
            TotalMatBReqPP1S = TotalMatBReqPP1S,
            TotalMatBReqPP2S = TotalMatBReqPP2S,
            TotalPARPMMatB = TotalPARPMMatB,
            TotalMatCReqPP1S = TotalMatCReqPP1S,
            TotalMatCReqPP2S = TotalMatCReqPP2S,
            TotalPARPMMatC = TotalPARPMMatC,
            MAPCMInvFinal1S = MAPCMInvFinal1S,
            MAPCMInvFinal2S = MAPCMInvFinal2S,
            MAPCMTotalMat1S = MAPCMTotalMat1S,
            MAPCMTotalMat2S = MAPCMTotalMat2S,
            MAPCMTotalMatAnual = MAPCMTotalMatAnual,
            MAPCMMatComp1S = MAPCMMatComp1S,
            MAPCMMatComp2S = MAPCMMatComp2S,
            MAPCMMatCompAnual = MAPCMMatCompAnual,
            MAPCMTotalEnPesos1S = MAPCMTotalEnPesos1S,
            MAPCMTotalEnPesos2S = MAPCMTotalEnPesos2S,
            MAPCMTotalEnPesosAnual = MAPCMTotalEnPesosAnual,
            MBPCMInvFinal1S = MBPCMInvFinal1S,
            MBPCMInvFinal2S = MBPCMInvFinal2S,
            MBPCMTotalMat1S = MBPCMTotalMat1S,
            MBPCMTotalMat2S = MBPCMTotalMat2S,
            MBPCMTotalMatAnual = MBPCMTotalMatAnual,
            MBPCMMatComp1S = MBPCMMatComp1S,
            MBPCMMatComp2S = MBPCMMatComp2S,
            MBPCMMatCompAnual = MBPCMMatCompAnual,
            MBPCMTotalEnPesos1S = MBPCMTotalEnPesos1S,
            MBPCMTotalEnPesos2S = MBPCMTotalEnPesos2S,
            MBPCMTotalEnPesosAnual = MBPCMTotalEnPesosAnual,
            MCPCMInvFinal1S = MCPCMInvFinal1S,
            MCPCMInvFinal2S = MCPCMInvFinal2S,
            MCPCMTotalMat1S = MCPCMTotalMat1S,
            MCPCMTotalMat2S = MCPCMTotalMat2S,
            MCPCMTotalMatAnual = MCPCMTotalMatAnual,
            MCPCMMatComp1S = MCPCMMatComp1S,
            MCPCMMatComp2S = MCPCMMatComp2S,
            MCPCMMatCompAnual = MCPCMMatCompAnual,
            MCPCMTotalEnPesos1S = MCPCMTotalEnPesos1S,
            MCPCMTotalEnPesos2S = MCPCMTotalEnPesos2S,
            MCPCMTotalEnPesosAnual = MCPCMTotalEnPesosAnual,
            TMPCM1S = TMPCM1S,
            TMPCM2S = TMPCM2S,
            TMPCMAnual = TMPCMAnual,
            DSPFSTotalProv2021 = DSPFSTotalProv2021,
            DSPFSPorProv2020 = DSPFSPorProv2020,
            DSPFSPorProv2021 = DSPFSPorProv2021,
            DSPFSTotalSalidas2021 = DSPFSTotalSalidas2021,
            DSPFSSaldoTotal2021 = DSPFSSaldoTotal2021,
            PAPMODTotalHorasRequer1S = PAPMODTotalHorasRequer1S,
            PAPMODTotalHorasRequer2S = PAPMODTotalHorasRequer2S,
            PAPMODTotalHorasRequerAnual = PAPMODTotalHorasRequerAnual,
            PAPMODHorasReq = PAPMODHorasReq,
            PAMODImporte1S = PAMODImporte1S,
            PAMODImporte2S = PAMODImporte2S,
            PAMODImporteAnual = PAMODImporteAnual,
            PBPMODTotalHorasRequer1S = PBPMODTotalHorasRequer1S,
            PBPMODTotalHorasRequer2S = PBPMODTotalHorasRequer2S,
            PBPMODTotalHorasRequerAnual = PBPMODTotalHorasRequerAnual,
            PBPMODHorasReq = PBPMODHorasReq,
            PBMODImporte1S = PBMODImporte1S,
            PBMODImporte2S = PBMODImporte2S,
            PBMODImporteAnual = PBMODImporteAnual,
            PCPMODTotalHorasRequer1S = PCPMODTotalHorasRequer1S,
            PCPMODTotalHorasRequer2S = PCPMODTotalHorasRequer2S,
            PCPMODTotalHorasRequerAnual = PCPMODTotalHorasRequerAnual,
            PCPMODHorasReq = PCPMODHorasReq,
            PCMODImporte1S = PCMODImporte1S,
            PCMODImporte2S = PCMODImporte2S,
            PCMODImporteAnual = PCMODImporteAnual,
            PMODTotalHoras1S = PMODTotalHoras1S,
            PMODTotalHoras2S = PMODTotalHoras2S,
            PMODTotalHorasAnual = PMODTotalHorasAnual,
            PMODTotalMOD1S = PMODTotalMOD1S,
            PMODTotalMOD2S = PMODTotalMOD2S,
            PMODTotalMODAnual = PMODTotalMODAnual)


if __name__ == ' __main__':
    app.debug = True
    app.run()