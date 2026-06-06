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

### Verse 1 (Vaivtpuran 543.14214)
- **Original**: मेरे लिये जैसे कचकी पत्नी (पुत्रवधू) रक्षणीय वाणामें बोले।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14215)
- **Original**: है, उसी प्रकार तुम भी हो। जो स्थान पुत्रका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14216)
- **Original**: 618 * संक्षिप्त ब्रह्मवैवर्तपुराण « है, वही शिष्यका भी है। तर्पण, पिण्डदान, पालन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14217)
- **Original**: तुम्हारी प्रतिष्ठा और यश लक्ष्मीजीके समान होंगे। और परितोषण-इन सभी कर्मोंके लिये पुत्र और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14218)
- **Original**: सौभाग्य और पतिविषयक प्रेम श्रीराधिकाके शिष्यमें कोई भेद नहीं है। जैसे पुत्र पिताके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14219)
- **Original**: समान होगा। स्वामीके प्रति गौरव, मान, प्रीति मरनेपर उसके लिये अग्निदाता होता है, अवश्य
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14220)
- **Original**: तथा प्रधानताका भाव भी तुममें श्रीराधाके ही उसी तरह शिष्य गुरुके लिये अग्निप्रदाता कहा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14221)
- **Original**: सदृश होगा। रोहिणीके समान तुममें पतिकी गया है। यह बात कण्वशाखामें ब्रह्माजीने कही
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14222)
- **Original**: अपेक्षा-बुद्धि होगी। तुम भारतीके समान है। पिता, माता, गुरु, पत्नी, छोटा बालक, अनाथ
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14223)
- **Original**: पूजनीया तथा सावित्रीके तुल्य सदा शुद्धा एवं एवं कुदुम्बीजन-ये पुरुषमात्रसे नित्य पोषण
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14224)
- **Original**: उपमारहित होओगी। पानेके योग्य हैं, ऐसा ब्रह्माजीका कथन है*।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14225)
- **Original**: . बृहस्पतिजी ऐसा कह ही रहे थे कि नहुषके जो इनका पोषण नहीं करता उसके शरीरके भस्म
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14226)
- **Original**: दूतने वहाँ आकर शचीसे नन्दनवनमें चलनेके होनेतक उसे सूतक (अशौच)-का भागी होना
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14227)
- **Original**: लिये कहा। यह सुनते ही बृहस्पतिजीका सारा पड़ता है। वह जीते-जी देवयज्ञ तथा पितृयज्ञमें
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14228)
- **Original**: शरीर क्रोध्से काँपने लगा और उनकी आँखें कर्म करनेका अधिकारी नहीं रहता है--ऐसा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14229)
- **Original**: लाल हो गयीं। वे उस दूतसे बोले। महेश्वरका कथन है। जो माता, पिता और गुरके। गुरुने कहा--दूत! तू जाकर नहुषसे कह प्रति मानव-बुद्धि रखता है, उसको सर्वत्र अयश
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14230)
- **Original**: दे कि 'महाराज ! यदि तुम शचीका उपभोग करना प्रात होता है और उसे पग-पगपर विप्नका ही (चाहते हो तो एक ऐसी सवारीपर चढ़कर रातमें सामना करना पड़ता है। जो सम्पत्तिसे मतवाला
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14231)
- **Original**: आना, जिसका आजसे पहले किसीने उपयोग होकर अपने गुरुका अपमान करता है, उसका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14232)
- **Original**: न किया हो। सप्तर्षियोंके कंधोंपर अपनी सुन्दर शीघ्र ही सर्वनाश हों जाता है; यह सुनिश्चित शिविका (पालकी) रख उत्तम वेशभूषासे सज- जात है। अपनी सभामें मुझे देखकर इन्द्र आसनसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14233)
- **Original**: धजकर उसीपर आरूढ़ हो तुम्हें यहाँतक यात्रा नहीं उठे थे, उसीका फल इस समय भोग रहे करनी चाहिये।' हैं। गुरुके अपमानका शीघ्र ही जो कु फल बृहस्पतिजीकी बात सुनकर दूतने नहुषके प्राप्त हुआ, उसे तुम अफ़ी आँखों देख लो।
- **Translation**: 

---

