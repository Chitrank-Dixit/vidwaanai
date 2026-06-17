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

### Verse 1 (Vaivtpuran 543.12674)
- **Original**: द्वारणलकी आज्ञासे ब्रह्मने भीतर आकर भक्तिभावसे शौघ्र ही आपके दर्पका दलन करेंगे। अन्य
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12675)
- **Original**: भगवान्‌की स्तुति की। उन्होंने ऐसे-ऐसे अति देवताओंकी प्रत्येक युगमें वार्षिक पूजा होगी;
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12676)
- **Original**: विचित्र स्तोत्र सुनाये, जो चतुर्मुख ब्रह्मेने कभी किंतु आपकी नहीं होगी। इस कल्पमें या
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12677)
- **Original**: नहीं सुने थे। स्तुति करके भगवान्‌ विष्णुकी आज्ञा कल्पान्तरमें, इस देहमें अथवा देहान्तरमें फिर पाकर बे चतुर्मुख ब्रह्मको पीछे करके बैठे। आपकी पूजा नहीं होगी। अबतक जो हो गयी,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12678)
- **Original**: तदनन्तर भगवान्‌ नारायणने अपने चार भुजाधारी सो हो गयी।' द्वारपालोंसे कहा--' जो कोई भी आगन्तुक सज्जन यों कहकर मोहिनी शौघ्र ही कामलोकमें हों, उन्हें आदरपूर्वक भीतर ले आओ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12679)
- **Original**: ।' गयी और पुनः सचेत होनेपर अपने कुकृत्यको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12680)
- **Original**: वृन्दावनविनोदिनि! इसी समय वहाँ अत्यन्त याद करके विलाप करने लगी। जगद्विधाता
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12681)
- **Original**: विनीतभावसे स्वयं शतमुख ब्रह्माका आगमन ब्रह्मा मोहिनीका शाप सुनकर काँप उठे। उनका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12682)
- **Original**: हुआ। उन्होंने भी अत्यन्त सुन्दर दिव्य स्तोत्रोंद्वारा मस्तक झुक गया। उस समय कल्याणकारी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12683)
- **Original**: गूढ़भावसे भगवान्‌का स्तवन किया। उनके मुखसे मुनियोंने उन्हें एक उपाय बताया--' आप भगवान्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12684)
- **Original**: निकले हुए श्रेष्ठ स्तोत्र सभीके लिये अश्रुतपूर्व वैकुण्ठनाथकी शरणमें जाइये।' ऐसा कहकर वे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12685)
- **Original**: (सर्वथा नवीन) थे। वे भी स्तुतिके पश्चात्‌ ऋषि-मुनि अपने-अपने आश्रमोंकों चले गये। भगवान्‌की आज्ञा पाकर पहलेके आये हुए दोनों तत्पश्चात्‌ ब्रह्माजी मेरे ही दूसरे स्वरूप परम शान्त
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12686)
- **Original**: ब्रह्माऑँके आगे बैठ गये। इसके बाद दूसरे किसी कमलाकान्त श्यामवर्ण भगवान्‌ नारायणकी शरणमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12687)
- **Original**: ब्रह्माण्डके अधिपति सहस्रमुख ब्रह्मा श्रीहरिके गये। वहाँ जा खिन्नचदन हो चार भुजाधारी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12688)
- **Original**: सामने उपस्थित हुए। उन्होंने भी भक्तिभावसे श्रीहरिकों प्रणाम करके वे जगत्स्राष्टा ब्रह्मा उनके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12689)
- **Original**: मस्तक झुकाकर किसीके द्वारा भी अबतक नहीं पास ही बैठे। उन्होंने विपत्तिसे उबारनेवाले,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12690)
- **Original**: सुने गये उत्तम स्तोत्रोंसे भगवान्‌की स्तुति की। (63] सं0 ज्र0 वै0 पुराण 9
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12691)
- **Original**: 556 + संक्षिप्त ब्रह्मवैवर्तपुराण * ##ऋ#ऋक#ऋऋ#ऋ#ऋऋ# ###%###################&##&#%&#&##%#######%&#&###%###### # ##### कक तत्पश्चात्‌ वे भी आज्ञा पाकर सबसे आगे बैठे।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12692)
- **Original**: अपने स्थानकों चले गये। चतुर्मुख ब्रह्माने उनसे श्रीहरिने समस्त ब्रह्माण्डोंके ब्रह्माेओंका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12693)
- **Original**: अपनेको अत्यन्त छोटा तथा अल्प राज्यका और उनके राज्यमें रहनेवाले देवताओंका क्रमश:
- **Translation**: 

---

