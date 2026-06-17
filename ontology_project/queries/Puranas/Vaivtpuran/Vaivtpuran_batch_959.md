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

### Verse 1 (Vaivtpuran 543.17494)
- **Original**: हैं; वे ही ये गोलोकनाथ श्रीकृष्ण गोकुलमें पीछे चली गयीं। जगत्‌के पालनकर्ता विष्णुके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17495)
- **Original**: वृन्दावन नामक पुण्यवनमें गोपवेष धारण करके श्वेतद्वीप चले जानेपर श्रीकृष्णके मनसे उत्पन्न हुई
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17496)
- **Original**: नन्दके पृत्ररूपसे अवतीर्ण हुए हैं। ये राधाके मनोहरा मर्त्यलक्ष्मीने भी उनका अनुगमन किया।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17497)
- **Original**: प्राणपति हैं। ये ही बैकुण्ठमें चार-भुजाधारी इस प्रकार उस शुद्ध सत्त्वस्वरूपके दो रूप हो
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17498)
- **Original**: महालक्ष्मीपति स्वयं भगवान्‌ नारायण हैं; जिनका गये। उनमें दक्षिणाज़ दो भुजाधारी गोप-बालकके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17499)
- **Original**: नाम मुक्ति-प्राप्तिका कारण है। रूपमें प्रकट हुआ। वह नूतन जलधरके समान नारद! जो मनुष्य एक बार भी 'नारायण' श्याम और पोीताम्बरसे शोभित था; उसके मुखसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17500)
- **Original**: नामका उच्चारण कर लेता है; वह तीन सौ सुन्दर वंशी लगी हुई थी; नेत्र कमलके समान
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17501)
- **Original**: कल्पोंतक गड़ा आदि सभी तीर्थोमें स्तान करनेका विशाल थे; बह शोभासम्पन्न तथा मन्द मुस्कानसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17502)
- **Original**: फल पा लेता है। तदनन्तर जो शझ्भु, चक्र, गदा युक्त था। वह सौ करोड़ चन्द्रमाओंके समान और पद्म धारण करते हैं; जिनके वक्ष:स्थलमें सौन्दर्यशाली, सौ करोड़ कामदेबोंकी-सी प्रभावाला,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17503)
- **Original**: श्रीवत्सका चिह्न शोभा देता है; मणिश्रेष्ठ कौस्तुभ परमानन्दस्वरूप, परिपूर्णतम, प्रभु, परमधाम,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17504)
- **Original**: और वनमालासे जो सुशोभित होते हैं; वेद पर्रह्मस्वरूप, निर्गुण, सबका परमात्मा, भक्तानुग्रहमूर्ति,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17505)
- **Original**: जिनकी स्तुति करते हैं; वे भगवान्‌ नारायण अविनाशी शरीरबाला, प्रकृतिसे पर और ऐश्वर्यशाली
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17506)
- **Original**: सुनन्‍्द, नन्‍्द और कुमुद आदि पार्षदोंके साथ ईश्वर था। योगीलोग जिसे सनातन ज्योतिरूप
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17507)
- **Original**: विमानद्वारा अपने स्थान वैकुण्ठको चले गये। उन जानते हैं और उस ज्योतिके भीतर जिसके नित्य
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17508)
- **Original**: बैकुण्ठनाथके चले जानेपर राधाके स्वामी स्वयं रूपको भक्तिके सहारे समझ पाते हैं। विचक्षण वेद
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17509)
- **Original**: श्रीकृष्णे अपनी वंशी बजायी, जिसका सुरीला जिसे सत्य, नित्य और आद्य बतलाते हैं, सभी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17510)
- **Original**: शब्द त्रिलोकीको मोहमें डालनेबाला था। नारद! देवता जिसे स्वेच्छामय परम प्रभु कहते हैं, सारे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17511)
- **Original**: उस शब्दको सुनते ही पार्वतीके अतिरिक्त सभी सिद्धशिरोमणि तथा मुनिवर जिसे सर्वरूप कहकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17512)
- **Original**: देवतागण और मुनिगण मूर्च्छित हो गये और पुकारते हैं, योगिराज शंकर जिसका नाम अनिर्वचनीय
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17513)
- **Original**: उनकी चेतना लुप्त हो गयी। तब जो भगवती रखते हैं, स्वयं ब्रह्मा जिसे कारणके कारणरूपसे
- **Translation**: 

---

