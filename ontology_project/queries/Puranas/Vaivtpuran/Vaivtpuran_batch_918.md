# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 543.16674)
- **Original**: नहीं ज्ञात होता। करके श्रीहरि महलके भीतर चले गये। राधिकाकी बात सुनकर नन्‍्दकों महान्‌ तब नन्दजों यशोदाके साथ कदलीबनको
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16675)
- **Original**: बिस्मय हुआ। तब गोपी यशोदा सम्भाषण करनेके गये। वहाँ उन्होंने राधाकों देखा, जो पह्लूस्थ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16676)
- **Original**: लिये डरते-डरते राधाके निकट गयीं और उनके चन्दनचर्चित जलबुक्त कमल-दलकी शब्यापर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16677)
- **Original**: पास ही बैठकर प्रिय वचन बोलीं। नन्‍्द भी अचेत हो शयन कर रही थीं। राधाने अपने
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16678)
- **Original**: वहीं यशोदाद्वारा दिये गये आसनपर बैठ गये। अड्जोंसे भूषणोंको उतार फेंका था, उनके शरीरपर श्रेत वस्त्र शोभा पा रहा था, आहारका त्याग
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16679)
- **Original**: कर देनेसे उनका ठदर कृश हो गया था, मूच्छितावस्थामें उनके ओष्ट सूख गये थे और नेत्रोंमें आँसू भरे हुए थे। वे परमात्मा श्रीकृष्णके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16680)
- **Original**: //? चरणकमलका ध्यान कर रही थीं, उनका चित्त
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16681)
- **Original**: ] कट पु एकमात्र उन्हींमें निविष्ट था और बाह्वाज्ञान लुप्त हि» हो गया था। वे बीच-बीचमें मुखकमलकों ऊपर ताक च््द उठाकर मन्द मुस्कानयुक्त प्रियतम श्रीकृष्णका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16682)
- **Original**: 5194 7: स्‍्प्प् 32234 मार्ग जोहती रहतो थीं। स्वप्रमें प्रियतमके समीप [[ ह्ड् पहुँचकर कभी हँसती और कभी रोती थीं। तब यशोदाने कहा--राधे ! चेत करो; तुम सख्ियाँ चारों ओरसे श्वेत चँंबरद्वारा निरन्तर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16683)
- **Original**: यलपूर्बक अपनी रक्षा करो; क्योंकि मड्भल दिन उनकी सेवा कर रही थीं। राधाकी यह दशा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16684)
- **Original**: आनेपर तुम अपने प्राणनाथके दर्शन करोगी। देखकर भार्यासहित नन्दको महान्‌ विस्मय हुआ।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16685)
- **Original**: सुरेध्वरि ! तुमने अपने कुल तथा विश्वकों पवित्र उन्होंने दण्डकी भाँति भूमिपर लेटकर परम
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16686)
- **Original**: कर दिया है। तुम्हीिरे चरणकमलकोौ सेवासे ये भक्तिके साथ राधाकों नमस्कार किया। उसी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16687)
- **Original**: गोपियाँ पुण्यवती हो गयी हैं। जनसमूह, संतगण, समय ईं श्वरेच्छासे सहसा राधाकौ नींद उचट गयी ।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16688)
- **Original**: चारों वेद और पुरातन पुराण तुम्हारी तीर्थोंको वे जाग पड़ीं और क्षणभरमें ही उन्हें विषयज्ञानरहित
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16689)
- **Original**: पावन बनानेवाली सुमड्गरल कीर्तिका गान करेंगे। चेतना प्राप्त हो गयी। तब वे उस सखी-समाजमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16690)
- **Original**: बुद्धिरूपे! मैं यशोदा हूँ, ये नन्‍्द हैं और तुम सामने पति-पत्नी नन्‍्द-यशोदाकों देखकर उनसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16691)
- **Original**: वृषभानुनन्दिनी राधा हो। सुव्रते! मेरी बात सुनो। आदरपूर्वक पूछते हुए मधुर वचन बोलौं। । भद्रे! मैं द्वारका नगरसे श्रीकृष्णके पाससे तुम्हारे आजतक माई का बात जुट क्र 926 । । 11 क्रीः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16692)
- **Original**: 73 * संक्षिप्त ब्रह्मवैवर्तपुराण * 54% 4 % $ ! 5 5 5 4 5 5 % $ 5 % 4 $ 5 5 $ हु $ $ $ $ $ $ $ 5 # # 95555 8 #######क# 4 # 5 588 54 4 444 $$ #$% 5 $ 45 44% निकट आयी हूँ। सति! श्रीहरिने ही मुझे तुम्हारे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16693)
- **Original**: शापसे “मुक्त हो जाओगी। इस प्रकार यशोदाके पास भेजा है। अब तुम उन गदाधरका मड़जल-
- **Translation**: 

---

