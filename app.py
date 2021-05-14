from flask import Flask, render_template, request

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

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

        TotalVentasPorSemestre1S = PAIV1S + PBIV1S + PBIV1S
        TotalVentasPorSemestre2S = PAIV2S + PBIV2S + PBIV2S
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

        PAPPPApresVenUnidVend1S = float(PApresVenUnidVend1S)
        PAPPPApresVenUnidVend2S = float(PApresVenUnidVend2S)
        PAPPUnidsAVender = float(PApresVenUnidVend1S) + float(PApresVenUnidVend2S)
        PAPPInvFinalTotal2021 = PAPPPApresVenUnidVend2S
        PAPPTotalUnidades1S = PAPPUnidsAVender + float(PAPPInvFinal1S)
        PAPPTotalUnidades2S = PAPPPApresVenUnidVend2S + float(PAPPInvFinal2S)
        PAPPTotalUnidades2021 = PAPPUnidsAVender + PAPPInvFinalTotal2021
        PAPPInvInicial2S = float(PAPPInvFinal1S)
        PAPPInvTotal2021 = float(PAPPInvInicial1S)
        PAPPUnidsAProducir1S = PAPPTotalUnidades1S - float(PAPPInvInicial1S)
        PAPPUnidsAProducir2S = PAPPTotalUnidades2S - float(PAPPInvInicial2S)
        PAPPUnidsAProducir2021 = PAPPTotalUnidades2021 - float(PAPPInvTotal2021)

        #Producto B    
        PBPPInvFinal1S = request.form['PBPPInvFinal1S']
        PBPPInvFinal2S = request.form['PBPPInvFinal2S']
        PBPPInvInicial1S = request.form['PBPPInvInicial1S']

        PBPPPApresVenUnidVend1S = float(PBpresVenUnidVend1S)
        PBPPPApresVenUnidVend2S = float(PBpresVenUnidVend2S)
        PBPPUnidsAVender = float(PBpresVenUnidVend1S) + float(PBpresVenUnidVend2S)
        PBPPInvFinalTotal2021 = PBPPPApresVenUnidVend2S
        PBPPTotalUnidades1S = PBPPUnidsAVender + float(PBPPInvFinal1S)
        PBPPTotalUnidades2S = PBPPPApresVenUnidVend2S + float(PBPPInvFinal2S)
        PBPPTotalUnidades2021 = PBPPUnidsAVender + PBPPInvFinalTotal2021
        PBPPInvInicial2S = float(PBPPInvFinal1S)
        PBPPInvTotal2021 = float(PBPPInvInicial1S)
        PBPPUnidsAProducir1S = PBPPTotalUnidades1S - float(PBPPInvInicial1S)
        PBPPUnidsAProducir2S = PBPPTotalUnidades2S - float(PBPPInvInicial2S)
        PBPPUnidsAProducir2021 = PBPPTotalUnidades2021 - float(PBPPInvTotal2021)

        #Producto C
        PCPPInvFinal1S = request.form['PCPPInvFinal1S']
        PCPPInvFinal2S = request.form['PCPPInvFinal2S']
        PCPPInvInicial1S = request.form['PCPPInvInicial1S']

        PCPPPApresVenUnidVend1S = float(PCpresVenUnidVend1S)
        PCPPPApresVenUnidVend2S = float(PCpresVenUnidVend2S)
        PCPPUnidsAVender = float(PCpresVenUnidVend1S) + float(PCpresVenUnidVend2S)
        PCPPInvFinalTotal2021 = PCPPPApresVenUnidVend2S
        PCPPTotalUnidades1S = PCPPUnidsAVender + float(PCPPInvFinal1S)
        PCPPTotalUnidades2S = PCPPPApresVenUnidVend2S + float(PCPPInvFinal2S)
        PCPPTotalUnidades2021 = PCPPUnidsAVender + PCPPInvFinalTotal2021
        PCPPInvInicial2S = float(PCPPInvFinal1S)
        PCPPInvTotal2021 = float(PCPPInvInicial1S)
        PCPPUnidsAProducir1S = PCPPTotalUnidades1S - float(PCPPInvInicial1S)
        PCPPUnidsAProducir2S = PCPPTotalUnidades2S - float(PCPPInvInicial2S)
        PCPPUnidsAProducir2021 = PCPPTotalUnidades2021 - float(PCPPInvTotal2021)

        # 4. Presupuesto de Requerimiento de Materiales

        #Producto A
        #Material A
        PAPRMReqMatA = request.form['PAPRMReqMatA']

        PAPRMTotalMatA1S = PAPPUnidsAProducir1S * float(PAPRMReqMatA)
        PAPRMTotalMatA2S = PAPPUnidsAProducir2S * float(PAPRMReqMatA)
        PAPRMTotalMatATotal = PAPPUnidsAProducir2021 * float(PAPRMReqMatA)
        
        #Material B
        PAPRMReqMatB = request.form['PAPRMReqMatB']

        PAPRMTotalMatB1S = PAPPUnidsAProducir1S * float(PAPRMReqMatB)
        PAPRMTotalMatB2S = PAPPUnidsAProducir2S * float(PAPRMReqMatB)
        PAPRMTotalMatBTotal = PAPPUnidsAProducir2021 * float(PAPRMReqMatB)

        #Material B
        PAPRMReqMatC = request.form['PAPRMReqMatC']

        PAPRMTotalMatC1S = PAPPUnidsAProducir1S * float(PAPRMReqMatC)
        PAPRMTotalMatC2S = PAPPUnidsAProducir2S * float(PAPRMReqMatC)
        PAPRMTotalMatCTotal = PAPPUnidsAProducir2021 * float(PAPRMReqMatC)

        #Producto B
        #Material A
        PBPRMReqMatA = request.form['PBPRMReqMatA']

        PBPRMTotalMatA1S = PBPPUnidsAProducir1S * float(PBPRMReqMatA)
        PBPRMTotalMatA2S = PBPPUnidsAProducir2S * float(PBPRMReqMatA)
        PBPRMTotalMatATotal = PBPPUnidsAProducir2021 * float(PBPRMReqMatA)
        
        #Material B
        PBPRMReqMatB = request.form['PBPRMReqMatB']

        PBPRMTotalMatB1S = PBPPUnidsAProducir1S * float(PBPRMReqMatB)
        PBPRMTotalMatB2S = PBPPUnidsAProducir2S * float(PBPRMReqMatB)
        PBPRMTotalMatBTotal = PBPPUnidsAProducir2021 * float(PBPRMReqMatB)

        #Material B
        PBPRMReqMatC = request.form['PBPRMReqMatC']

        PBPRMTotalMatC1S = PBPPUnidsAProducir1S * float(PBPRMReqMatC)
        PBPRMTotalMatC2S = PBPPUnidsAProducir2S * float(PBPRMReqMatC)
        PBPRMTotalMatCTotal = PBPPUnidsAProducir2021 * float(PBPRMReqMatC)

        #Producto C
        #Material A
        PCPRMReqMatA = request.form['PCPRMReqMatA']

        PCPRMTotalMatA1S = PCPPUnidsAProducir1S * float(PCPRMReqMatA)
        PCPRMTotalMatA2S = PCPPUnidsAProducir2S * float(PCPRMReqMatA)
        PCPRMTotalMatATotal = PCPPUnidsAProducir2021 * float(PCPRMReqMatA)
        
        #Material B
        PCPRMReqMatB = request.form['PCPRMReqMatB']

        PCPRMTotalMatB1S = PCPPUnidsAProducir1S * float(PCPRMReqMatB)
        PCPRMTotalMatB2S = PCPPUnidsAProducir2S * float(PCPRMReqMatB)
        PCPRMTotalMatBTotal = PCPPUnidsAProducir2021 * float(PCPRMReqMatB)

        #Material B
        PCPRMReqMatC = request.form['PCPRMReqMatC']

        PCPRMTotalMatC1S = PCPPUnidsAProducir1S * float(PCPRMReqMatC)
        PCPRMTotalMatC2S = PCPPUnidsAProducir2S * float(PCPRMReqMatC)
        PCPRMTotalMatCTotal = PCPPUnidsAProducir2021 * float(PCPRMReqMatC)

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

        MAPCMTotalMat1S = TotalMatAReqPP1S + float(MAPCMInvFinal1S)
        MAPCMTotalMat2S = TotalMatAReqPP2S + float(MAPCMInvFinal2S)
        MAPCMTotalMatAnual = TotalPARPMMatA + float(MAPCMInvFinal2S)
        MAPCMMatComp1S = MAPCMTotalMat1S - float(MAPCMInvFinal1S)
        MAPCMMatComp2S = MAPCMTotalMat2S - float(MAPCMInvFinal1S)
        MAPCMMatCompAnual = MAPCMTotalMatAnual - float(MAPCMInvFinal1S)
        MAPCMTotalEnPesos1S = MAPCMMatComp1S * float(MAPCMPrecioComp1S)
        MAPCMTotalEnPesos2S = MAPCMMatComp2S * float(MAPCMPrecioComp2S)
        MAPCMTotalEnPesosAnual = MAPCMTotalEnPesos1S + MAPCMTotalEnPesos2S

        #Material B
        MBPCMInvFinal1S = request.form['MBPCMInvFinal1S']
        MBPCMInvFinal2S = request.form['MBPCMInvFinal2S']
        MBPCMPrecioComp1S = request.form['MBPCMPrecioComp1S']
        MBPCMPrecioComp2S = request.form['MBPCMPrecioComp2S']

        MBPCMTotalMat1S = TotalMatBReqPP1S + float(MBPCMInvFinal1S)
        MBPCMTotalMat2S = TotalMatBReqPP2S + float(MBPCMInvFinal2S)
        MBPCMTotalMatAnual = TotalPARPMMatB + float(MBPCMInvFinal2S)
        MBPCMMatComp1S = MBPCMTotalMat1S - float(MBPCMInvFinal1S)
        MBPCMMatComp2S = MBPCMTotalMat2S - float(MBPCMInvFinal1S)
        MBPCMMatCompAnual = MBPCMTotalMatAnual - float(MBPCMInvFinal1S)
        MBPCMTotalEnPesos1S = MBPCMMatComp1S * float(MBPCMPrecioComp1S)
        MBPCMTotalEnPesos2S = MBPCMMatComp2S * float(MBPCMPrecioComp2S)
        MBPCMTotalEnPesosAnual = MBPCMTotalEnPesos1S + MBPCMTotalEnPesos2S

        #Material C
        MCPCMInvFinal1S = request.form['MCPCMInvFinal1S']
        MCPCMInvFinal2S = request.form['MCPCMInvFinal2S']
        MCPCMPrecioComp1S = request.form['MCPCMPrecioComp1S']
        MCPCMPrecioComp2S = request.form['MCPCMPrecioComp2S']

        MCPCMTotalMat1S = TotalMatCReqPP1S + float(MCPCMInvFinal1S)
        MCPCMTotalMat2S = TotalMatCReqPP2S + float(MCPCMInvFinal2S)
        MCPCMTotalMatAnual = TotalPARPMMatC + float(MCPCMInvFinal2S)
        MCPCMMatComp1S = MCPCMTotalMat1S - float(MCPCMInvFinal1S)
        MCPCMMatComp2S = MCPCMTotalMat2S - float(MCPCMInvFinal1S)
        MCPCMMatCompAnual = MCPCMTotalMatAnual - float(MCPCMInvFinal1S)
        MCPCMTotalEnPesos1S = MCPCMMatComp1S * float(MCPCMPrecioComp1S)
        MCPCMTotalEnPesos2S = MBPCMMatComp2S * float(MCPCMPrecioComp2S)
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


        PAPMODTotalHorasRequer1S = PAPPUnidsAProducir1S * float(PAPMODHorasReq)
        PAPMODTotalHorasRequer2S = PAPPUnidsAProducir2S * float(PAPMODHorasReq)
        PAPMODTotalHorasRequerAnual = PAPPUnidsAProducir2021 * float(PAPMODHorasReq)
        PAMODImporte1S = float(PAPMODTotalHorasRequer1S) * float(PAPMODCuotaHora1S)
        PAMODImporte2S = float(PAPMODTotalHorasRequer2S) * float(PAPMODCuotaHora2S)
        PAMODImporteAnual = PAMODImporte1S + PAMODImporte2S

        #Producto B 
        PBPMODHorasReq = request.form['PBPMODHorasReq']
        PBPMODCuotaHora1S = request.form['PBPMODCuotaHora1S']
        PBPMODCuotaHora2S = request.form['PBPMODCuotaHora2S']


        PBPMODTotalHorasRequer1S = PBPPUnidsAProducir1S * float(PBPMODHorasReq)
        PBPMODTotalHorasRequer2S = PBPPUnidsAProducir2S * float(PBPMODHorasReq)
        PBPMODTotalHorasRequerAnual = PBPPUnidsAProducir2021 * float(PBPMODHorasReq)
        PBMODImporte1S = float(PBPMODTotalHorasRequer1S) * float(PBPMODCuotaHora1S)
        PBMODImporte2S = float(PBPMODTotalHorasRequer2S) * float(PBPMODCuotaHora2S)
        PBMODImporteAnual = PBMODImporte1S + PBMODImporte2S

        #Producto C
        PCPMODHorasReq = request.form['PCPMODHorasReq']
        PCPMODCuotaHora1S = request.form['PCPMODCuotaHora1S']
        PCPMODCuotaHora2S = request.form['PCPMODCuotaHora2S']

        PCPMODTotalHorasRequer1S = PCPPUnidsAProducir1S * float(PCPMODHorasReq)
        PCPMODTotalHorasRequer2S = PCPPUnidsAProducir2S * float(PCPMODHorasReq)
        PCPMODTotalHorasRequerAnual = PCPPUnidsAProducir2021 * float(PCPMODHorasReq)
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

        # 8. Presupuesto de Gastos Indirectos de Fabricación

        PGIFDepreciacionAnual = request.form['PGIFDepreciacionAnual']

        PGIFDepreciacion1S = float(PGIFDepreciacionAnual) / 2
        PGIFDepreciacion2S = PGIFDepreciacion1S

        PGIFSegurosAnual = request.form['PGIFSegurosAnual']

        PGIFSeguros1S = float(PGIFSegurosAnual) / 2
        PGIFSeguros2S = PGIFSeguros1S

        PGIFMantenimientoAnual = request.form['PGIFMantenimientoAnual']

        PGIFMantenimiento1S = float(PGIFMantenimientoAnual) / 2
        PGIFMantenimiento2S = PGIFMantenimiento1S

        PGIFEnergeticos1S = request.form['PGIFEnergeticos1S']
        PGIFEnergeticos2S = request.form['PGIFEnergeticos2S']
        PGIFEnergeticosAnual = float(PGIFEnergeticos1S) + float(PGIFEnergeticos2S)

        PGIFVariosAnual = request.form['PGIFVariosAnual']

        PGIFVarios1S = float(PGIFVariosAnual) / 2
        PGIFVarios2S = PGIFVarios1S

        PGIFTotalGIFPorSem1S = PGIFDepreciacion1S + PGIFSeguros1S + PGIFMantenimiento1S + float(PGIFEnergeticos1S) + PGIFVarios1S
        PGIFTotalGIFPorSem2S = PGIFDepreciacion2S + PGIFDepreciacion2S + PGIFMantenimiento2S + float(PGIFEnergeticos2S)+ PGIFVarios2S
        PGIFTotalGIFPorSemAnual = PGIFTotalGIFPorSem1S + PGIFTotalGIFPorSem2S

        PGIFCostoPorHoraGIF = PGIFTotalGIFPorSemAnual / PMODTotalHorasAnual

        # 9. Presupuesto de Gastos de Operación

        PGODepreciacionAnual = request.form['PGODepreciacionAnual']
        PGODepreciacion1S = float(PGODepreciacionAnual) / 2
        PGODepreciacion2S = PGODepreciacion1S

        PGOSueldosAnual = request.form['PGOSueldosAnual']
        PGOSueldos1S = float(PGOSueldosAnual) / 2
        PGOSueldos2S = PGOSueldos1S

        PGOComisiones1S = (TotalVentasPorSemestre1S * 1) / 100
        PGOComisiones2S = (TotalVentasPorSemestre2S * 1) / 100
        PGOComisionesAnual = PGOComisiones1S + PGOComisiones2S

        PGOVarios1S = request.form['PGOVarios1S']
        PGOVarios2S = request.form['PGOVarios2S']

        PGOVariosAnual = float(PGOVarios1S) + float(PGOVarios2S)

        PGOPrestamoAnual = request.form['PGOPrestamoAnual']

        PGOPrestamo1S = float(PGOPrestamoAnual) / 2
        PGOPrestamo2S = PGOPrestamo1S

        PGOTotal1S = PGODepreciacion1S + PGOSueldos1S + PGOComisiones1S + float(PGOVarios1S) + PGOPrestamo1S
        PGOTotal2S = PGODepreciacion2S + PGOSueldos2S + PGOComisiones2S + float(PGOVarios2S) + PGOPrestamo2S
        PGOTotalAnual = PGOTotal1S + PGOTotal2S

        # 10. Determinación del Costo Unitario de Productos Terminados
        #Producto A
        PAMADCUPTCosto = request.form['PAMADCUPTCosto']
        PAMADCUPTCantidad = request.form['PAMADCUPTCantidad']
        PAMADCUPTCostoUni = float(PAMADCUPTCosto) * float(PAMADCUPTCantidad)

        PAMBDCUPTCosto = request.form['PAMBDCUPTCosto']
        PAMBDCUPTCantidad = request.form['PAMBDCUPTCantidad']
        PAMBDCUPTCostoUni = float(PAMBDCUPTCosto) * float(PAMBDCUPTCantidad)
        
        PAMCDCUPTCosto = request.form['PAMCDCUPTCosto']
        PAMCDCUPTCantidad = request.form['PAMCDCUPTCantidad']
        PAMCDCUPTCostoUni = float(PAMCDCUPTCosto) * float(PAMCDCUPTCantidad)

        PAManoObraDCUPTCosto = request.form['PAManoObraDCUPTCosto']
        PAManoObraDCUPTCantidad = request.form['PAManoObraDCUPTCantidad']
        PAManoObraDCUPTCostUni = float(PAManoObraDCUPTCosto) * float(PAManoObraDCUPTCantidad)

        PAGastoIndDCUPTCostoUni = PGIFCostoPorHoraGIF * float(PAManoObraDCUPTCantidad)

        PACostoUniDCUPTCostoUni = PAMADCUPTCostoUni + PAMBDCUPTCostoUni + PAMCDCUPTCostoUni + PAManoObraDCUPTCostUni + PAGastoIndDCUPTCostoUni

        #Producto B
        PBMADCUPTCosto = request.form['PBMADCUPTCosto']
        PBMADCUPTCantidad = request.form['PBMADCUPTCantidad']
        PBMADCUPTCostoUni = float(PBMADCUPTCosto) * float(PBMADCUPTCantidad)

        PBMBDCUPTCosto = request.form['PBMBDCUPTCosto']
        PBMBDCUPTCantidad = request.form['PBMBDCUPTCantidad']
        PBMBDCUPTCostoUni = float(PAMBDCUPTCosto) * float(PBMBDCUPTCantidad)
        
        PBMCDCUPTCosto = request.form['PBMCDCUPTCosto']
        PBMCDCUPTCantidad = request.form['PBMCDCUPTCantidad']
        PBMCDCUPTCostoUni = float(PBMCDCUPTCosto) * float(PBMCDCUPTCantidad)

        PBManoObraDCUPTCosto = request.form['PBManoObraDCUPTCosto']
        PBManoObraDCUPTCantidad = request.form['PBManoObraDCUPTCantidad']
        PBManoObraDCUPTCostUni = float(PBManoObraDCUPTCosto) * float(PBManoObraDCUPTCantidad)

        PBGastoIndDCUPTCostoUni = PGIFCostoPorHoraGIF * float(PBManoObraDCUPTCantidad)

        PBCostoUniDCUPTCostoUni = PBMADCUPTCostoUni + PBMBDCUPTCostoUni + PBMCDCUPTCostoUni + PBManoObraDCUPTCostUni + PBGastoIndDCUPTCostoUni

        #Producto C
        PCMADCUPTCosto = request.form['PCMADCUPTCosto']
        PCMADCUPTCantidad = request.form['PCMADCUPTCantidad']
        PCMADCUPTCostoUni = float(PCMADCUPTCosto) * float(PCMADCUPTCantidad)

        PCMBDCUPTCosto = request.form['PCMBDCUPTCosto']
        PCMBDCUPTCantidad = request.form['PCMBDCUPTCantidad']
        PCMBDCUPTCostoUni = float(PCMBDCUPTCosto) * float(PCMBDCUPTCantidad)
        
        PCMCDCUPTCosto = request.form['PCMCDCUPTCosto']
        PCMCDCUPTCantidad = request.form['PCMCDCUPTCantidad']
        PCMCDCUPTCostoUni = float(PCMCDCUPTCosto) * float(PCMCDCUPTCantidad)

        PCManoObraDCUPTCosto = request.form['PCManoObraDCUPTCosto']
        PCManoObraDCUPTCantidad = request.form['PCManoObraDCUPTCantidad']
        PCManoObraDCUPTCostUni = float(PCManoObraDCUPTCosto) * float(PCManoObraDCUPTCantidad)

        PCGastoIndDCUPTCostoUni = PGIFCostoPorHoraGIF * float(PCManoObraDCUPTCantidad)

        PCCostoUniDCUPTCostoUni = PCMADCUPTCostoUni + PCMBDCUPTCostoUni + PCMCDCUPTCostoUni + PCManoObraDCUPTCostUni + PCGastoIndDCUPTCostoUni

        #11. Valuación de Inventarios Finales

        MAVIFCostoTotal = float(MAPCMInvFinal2S) * float(PAMADCUPTCantidad)
        MBVIFCostoTotal = float(MBPCMInvFinal2S) * float(PAMBDCUPTCantidad)
        MCVIFCostoTotal = float(MCPCMInvFinal2S) * float(PAMCDCUPTCantidad)
        VIFInvFinalMat = MAVIFCostoTotal + MBVIFCostoTotal + MCVIFCostoTotal

        PAVIFCostoTotal = float(PAPPInvFinal2S) * float(PACostoUniDCUPTCostoUni)
        PBVIFCostoTotal = float(PBPPInvFinal2S) * float(PBCostoUniDCUPTCostoUni)
        PCVIFCostoTotal = float(PCPPInvFinal2S) * float(PCCostoUniDCUPTCostoUni)

        VIFInvFinalProd = PAVIFCostoTotal + PBVIFCostoTotal + PCVIFCostoTotal

        #Presupuesto Financiero
        #Estado de Costo de Producciony ventas
        ECPVSaldoInicialMat = request.form['ECPVSaldoInicialMat']
        ECPVInvInicPT = request.form['ECPVInvInicPT']
        
        ECPVMaterialDisp = float(ECPVSaldoInicialMat) + TMPCMAnual
        ECPVMaterialesUtil = ECPVMaterialDisp - VIFInvFinalMat
        ECPVCostoProduccion = ECPVMaterialesUtil + PMODTotalMODAnual + PGIFTotalGIFPorSemAnual
        ECPVTotalProdDisp = ECPVCostoProduccion + float(ECPVInvInicPT)
        ECPVCostoVentas = float(ECPVTotalProdDisp) - float(VIFInvFinalProd)

        #Estado de Resultados
        ERUtilidadBruta = TotalVentasPorSemestre - ECPVCostoVentas
        ERUtilidadOperacion = ERUtilidadBruta - PGOTotalAnual

        ISRPorcentaje = request.form['ISRPorcentaje']

        ERISRCalc = ERUtilidadOperacion * (float(ISRPorcentaje) / 100)
        ERPTUCalc = ERUtilidadOperacion * 0.1
        ERUtilidadNeta = ERUtilidadOperacion - ERISRCalc - ERPTUCalc

        #Estado de Flujo de Efectivo
        EFESaldoIni = request.form['EFESaldoIni']
        EFECompraAvtivoFij = request.form['EFECompraAvtivoFij']
        EFEPAGOISR = request.form['EFEPAGOISR']

        EFETotalEntradas = DSCFECobranza2021 + float(DSCFESaldo2020)
        EFEEfectivoDisp = float(EFESaldoIni) + EFETotalEntradas
        EFEPagoGIF = PGIFTotalGIFPorSemAnual - float(PGIFDepreciacionAnual)
        EFEPagoGO = PGOTotalAnual - float(PGODepreciacionAnual)
        EFETotalSalidas = DSPFSPorProv2021 + DSPFSPorProv2020 + PMODTotalMODAnual + EFEPagoGIF + EFEPagoGO + float(EFECompraAvtivoFij) + float(EFEPAGOISR)
        EFETotalFlujo = EFEEfectivoDisp - EFETotalSalidas

        #Balance General
        BGDuedoresDiv = request.form['BGDuedoresDiv']
        BGFuncionariosEmp = request.form['BGFuncionariosEmp']
        BGTerreno = request.form['BGTerreno']
        BGPlantaEquipo = request.form['BGPlantaEquipo']
        BGDepreciaAcum = request.form['BGDepreciaAcum']
        BGDocPorPagar = request.form['BGDocPorPagar']
        BGPrestamoBanc = request.form['BGPrestamoBanc']
        BGCapCont = request.form['BGCapCont']
        BGCapGan = request.form['BGCapGan']


        BGTerreno = float(BGTerreno)
        BGTotalActCir = EFETotalFlujo + DSCFESaldoClientes2021 + float(BGDuedoresDiv) + float(BGFuncionariosEmp) + VIFInvFinalMat + VIFInvFinalProd
        BGPlantaEquipoCalc = float(BGPlantaEquipo) + float(EFECompraAvtivoFij)
        BGTotalDepreciacion = (float(BGDepreciaAcum) + float(PGODepreciacionAnual) + float(PGIFDepreciacionAnual) * -1)
        BGTotalActivosNoCir = BGTerreno + BGPlantaEquipoCalc + BGTotalDepreciacion
        BGActivoTotal = BGTotalActCir + BGTotalActivosNoCir
        BGTotalPasivCP = DSPFSSaldoTotal2021 + float(BGDocPorPagar) + ERISRCalc + ERPTUCalc
        BFTotalCapCon = ERUtilidadNeta + float(BGCapCont) + float(BGCapGan)
        BGPasivoTotal = float(BGPrestamoBanc) + BGTotalPasivCP
        BGSumaPyC = BGPasivoTotal + BFTotalCapCon


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
            TotalVentasPorSemestre1S = TotalVentasPorSemestre1S,
            TotalVentasPorSemestre2S = TotalVentasPorSemestre2S,
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
            PMODTotalMODAnual = PMODTotalMODAnual,
            PGIFDepreciacion1S = PGIFDepreciacion1S,
            PGIFDepreciacion2S = PGIFDepreciacion2S,
            PGIFSeguros1S = PGIFSeguros1S,
            PGIFSeguros2S = PGIFSeguros2S,
            PGIFMantenimiento1S = PGIFMantenimiento1S,
            PGIFMantenimiento2S = PGIFMantenimiento2S,
            PGIFEnergeticosAnual = PGIFEnergeticosAnual,
            PGIFVarios1S = PGIFVarios1S,
            PGIFVarios2S = PGIFVarios2S,
            PGIFTotalGIFPorSem1S = PGIFTotalGIFPorSem1S,
            PGIFTotalGIFPorSem2S = PGIFTotalGIFPorSem2S,
            PGIFTotalGIFPorSemAnual = PGIFTotalGIFPorSemAnual,
            PGIFCostoPorHoraGIF = PGIFCostoPorHoraGIF,
            PGODepreciacion1S = PGODepreciacion1S,
            PGODepreciacion2S = PGODepreciacion2S,
            PGOSueldos1S = PGOSueldos1S,
            PGOSueldos2S = PGOSueldos2S,
            PGOComisiones1S = PGOComisiones1S,
            PGOComisiones2S = PGOComisiones2S,
            PGOComisionesAnual = PGOComisionesAnual,
            PGOVariosAnual = PGOVariosAnual,
            PGOPrestamo1S = PGOPrestamo1S,
            PGOPrestamo2S = PGOPrestamo2S,
            PGOTotal1S = PGOTotal1S,
            PGOTotal2S = PGOTotal2S,
            PGOTotalAnual = PGOTotalAnual,
            PAMADCUPTCostoUni = PAMADCUPTCostoUni,
            PAMBDCUPTCostoUni = PAMBDCUPTCostoUni,
            PAMCDCUPTCostoUni = PAMCDCUPTCostoUni,
            PAManoObraDCUPTCostUni = PAManoObraDCUPTCostUni,
            PAGastoIndDCUPTCostoUni = PAGastoIndDCUPTCostoUni,
            PAManoObraDCUPTCantidad = PAManoObraDCUPTCantidad,
            PACostoUniDCUPTCostoUni = PACostoUniDCUPTCostoUni,
            PBMADCUPTCostoUni = PBMADCUPTCostoUni,
            PBMBDCUPTCostoUni = PBMBDCUPTCostoUni,
            PBMCDCUPTCostoUni = PBMCDCUPTCostoUni,
            PBManoObraDCUPTCostUni = PBManoObraDCUPTCostUni,
            PBGastoIndDCUPTCostoUni = PBGastoIndDCUPTCostoUni,
            PBManoObraDCUPTCantidad = PBManoObraDCUPTCantidad,
            PBCostoUniDCUPTCostoUni = PBCostoUniDCUPTCostoUni,
            PCMADCUPTCostoUni = PCMADCUPTCostoUni,
            PCMBDCUPTCostoUni = PCMBDCUPTCostoUni,
            PCMCDCUPTCostoUni = PCMCDCUPTCostoUni,
            PCManoObraDCUPTCostUni = PCManoObraDCUPTCostUni,
            PCGastoIndDCUPTCostoUni = PCGastoIndDCUPTCostoUni,
            PCManoObraDCUPTCantidad = PCManoObraDCUPTCantidad,
            PCCostoUniDCUPTCostoUni = PCCostoUniDCUPTCostoUni,
            PAMADCUPTCantidad = PAMADCUPTCantidad,
            MAVIFCostoTotal = MAVIFCostoTotal,
            PAMBDCUPTCantidad = PAMBDCUPTCantidad,
            MBVIFCostoTotal = MBVIFCostoTotal,
            PAMCDCUPTCantidad = PAMCDCUPTCantidad,
            MCVIFCostoTotal = MCVIFCostoTotal,
            VIFInvFinalMat = VIFInvFinalMat,
            PAPPInvFinal2S = PAPPInvFinal2S,
            PAVIFCostoTotal = PAVIFCostoTotal,
            PBVIFCostoTotal = PBVIFCostoTotal,
            PBPPInvFinal2S = PBPPInvFinal2S,
            PCPPInvFinal2S = PCPPInvFinal2S,
            PCVIFCostoTotal = PCVIFCostoTotal,
            VIFInvFinalProd = VIFInvFinalProd,
            ECPVMaterialDisp = ECPVMaterialDisp,
            ECPVMaterialesUtil = ECPVMaterialesUtil,
            ECPVCostoProduccion = ECPVCostoProduccion,
            ECPVTotalProdDisp = ECPVTotalProdDisp,
            ECPVCostoVentas = ECPVCostoVentas,
            ERUtilidadBruta = ERUtilidadBruta,
            ERUtilidadOperacion = ERUtilidadOperacion,
            ERISRCalc = ERISRCalc,
            ERPTUCalc = ERPTUCalc,
            ERUtilidadNeta = ERUtilidadNeta,
            EFETotalEntradas = EFETotalEntradas,
            EFEEfectivoDisp = EFEEfectivoDisp,
            EFEPagoGIF = EFEPagoGIF,
            EFEPagoGO = EFEPagoGO,
            EFETotalSalidas = EFETotalSalidas,
            EFETotalFlujo = EFETotalFlujo,
            BGTotalActCir = BGTotalActCir,
            BGPlantaEquipoCalc = BGPlantaEquipoCalc,
            BGTerreno = BGTerreno,
            BGTotalDepreciacion = BGTotalDepreciacion,
            BGTotalActivosNoCir = BGTotalActivosNoCir,
            BGActivoTotal = BGActivoTotal,
            BGDocPorPagar = float(BGDocPorPagar),
            BGTotalPasivCP = BGTotalPasivCP,
            BGPrestamoBanc = float(BGPrestamoBanc),
            BGCapCont = float(BGCapCont),
            BGCapGan= float(BGCapGan),
            BFTotalCapCon = BFTotalCapCon,
            BGPasivoTotal = BGPasivoTotal,
            BGSumaPyC = BGSumaPyC,
            PApresVenUnidVend1S = PApresVenUnidVend1S,
            PApresVenUnidVend2S = PApresVenUnidVend2S,
            PApresVenPrecVent1S = PApresVenPrecVent1S,
            PApresVenPrecVent2S = PApresVenPrecVent2S,
            PBpresVenUnidVend1S = PBpresVenUnidVend1S,
            PBpresVenUnidVend2S = PBpresVenUnidVend2S,
            PBpresVenPrecVent1S = PBpresVenPrecVent1S,
            PBpresVenPrecVent2S = PBpresVenPrecVent2S,
            PCpresVenUnidVend1S = PCpresVenUnidVend1S,
            PCpresVenUnidVend2S = PCpresVenUnidVend2S,
            PCpresVenPrecVent1S = PCpresVenPrecVent1S,
            PCpresVenPrecVent2S = PCpresVenPrecVent2S,
            DSCFEPorcentaje2020 = DSCFEPorcentaje2020,
            DSCFEPorcentaje2021 = DSCFEPorcentaje2021,
            PAPPInvFinal1S = PAPPInvFinal1S,
            PAPPInvInicial1S = PAPPInvInicial1S,
            PBPPInvFinal1S = PBPPInvFinal1S,
            PBPPInvInicial1S = PBPPInvInicial1S,
            PCPPInvInicial1S = PCPPInvInicial1S,
            PAPRMReqMatB = PAPRMReqMatB,
            PAPRMReqMatC = PAPRMReqMatC,
            PCPRMReqMatB = PCPRMReqMatB,
            PCPRMReqMatC = PCPRMReqMatC,
            MAPCMPrecioComp1S = MAPCMPrecioComp1S,
            MAPCMPrecioComp2S = MAPCMPrecioComp2S,
            MBPCMPrecioComp1S = MBPCMPrecioComp1S,
            MBPCMPrecioComp2S = MBPCMPrecioComp2S,
            MCPCMPrecioComp1S = MCPCMPrecioComp1S,
            MCPCMPrecioComp2S = MCPCMPrecioComp2S,
            DSPFSSaldoProvTotal2020 = DSPFSSaldoProvTotal2020,
            DSPFSPorceProv2020 = DSPFSPorceProv2020,
            DSPFSPorceProv2021 = DSPFSPorceProv2021,
            PAPMODCuotaHora1S = PAPMODCuotaHora1S,
            PAPMODCuotaHora2S = PAPMODCuotaHora2S,
            PBPMODCuotaHora1S = PBPMODCuotaHora1S,
            PBPMODCuotaHora2S = PBPMODCuotaHora2S,
            PCPMODCuotaHora1S = PCPMODCuotaHora1S,
            PCPMODCuotaHora2S = PCPMODCuotaHora2S,
            PGIFDepreciacionAnual = PGIFDepreciacionAnual,
            PGIFSegurosAnual = PGIFSegurosAnual,
            PGIFMantenimientoAnual = PGIFMantenimientoAnual,
            PGIFEnergeticos1S = PGIFEnergeticos1S,
            PGIFEnergeticos2S = PGIFEnergeticos2S,
            PGIFVariosAnual = PGIFVariosAnual,
            PGODepreciacionAnual = PGODepreciacionAnual,
            PGOSueldosAnual = PGOSueldosAnual,
            PGOVarios1S = PGOVarios1S,
            PGOVarios2S = PGOVarios2S,
            PGOPrestamoAnual = PGOPrestamoAnual,
            PAMADCUPTCosto = PAMADCUPTCosto,
            PAMBDCUPTCosto = PAMBDCUPTCosto,
            PAMCDCUPTCosto = PAMCDCUPTCosto,
            PAManoObraDCUPTCosto = PAManoObraDCUPTCosto,
            PBMADCUPTCosto = PBMADCUPTCosto,
            PBMADCUPTCantidad = PBMADCUPTCantidad,
            PBMBDCUPTCosto = PBMBDCUPTCosto,
            PBMBDCUPTCantidad = PBMBDCUPTCantidad,
            PBMCDCUPTCosto = PBMCDCUPTCosto,
            PBMCDCUPTCantidad = PBMCDCUPTCantidad,
            PBManoObraDCUPTCosto = PBManoObraDCUPTCosto,
            PCMADCUPTCosto = PCMADCUPTCosto,
            PCMADCUPTCantidad = PCMADCUPTCantidad,
            PCMBDCUPTCosto = PCMBDCUPTCosto,
            PCMBDCUPTCantidad = PCMBDCUPTCantidad,
            PCMCDCUPTCosto = PCMCDCUPTCosto,
            PCMCDCUPTCantidad = PCMCDCUPTCantidad,
            PCManoObraDCUPTCosto = PCManoObraDCUPTCosto,
            ECPVSaldoInicialMat = ECPVSaldoInicialMat,
            ECPVInvInicPT = ECPVInvInicPT,
            EFECompraAvtivoFij = EFECompraAvtivoFij,
            EFEPAGOISR = EFEPAGOISR,
            BGDuedoresDiv = BGDuedoresDiv,
            BGFuncionariosEmp = BGFuncionariosEmp,
            BGPlantaEquipo = BGPlantaEquipo,
            BGDepreciaAcum = BGDepreciaAcum,
            EFESaldoIni = EFESaldoIni,
            PCPPInvFinal1S = PCPPInvFinal1S)