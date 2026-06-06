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

### Verse 1 (Vaivtpuran 115.654)
- **Original**: प्रदान करनेवाले हैं। विस्तारपूर्वक वर्णन करता हूँ; सुनिये। उन्हें देखते ही गन्धर्बने सहसा दण्डकी इन दिनों जो गन्धर्वराज थे, वे सब गन्थवाँमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 115.655)
- **Original**: भाँति पृथ्वीपर पड़कर प्रणाम किया और वसिष्ठजीके श्रेष्ठ और महान्‌ थे, उच्चकोटिके ऐश्वर्यसे सम्पन्न [दिये हुए स्तोत्रसे उन परमेश्वरका स्तवन किया। थे, परंतु किसी कर्मवश पुत्र-सुखसे वज्षित थे।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 115.656)
- **Original**: तब कृपानिधान शिव उससे बोले--'गन्धर्वराज! एक समय गुरुकी आज्ञा लेकर बे पुष्करतीर्थमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 115.657)
- **Original**: तुम कोई वर माँगो।' तब गन्धर्वने उनसे भगवान्‌ गये और वहाँ उत्तम समाधि लगाकर (अथवा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 115.658)
- **Original**: श्रीहरिकी भक्ति तथा परम वैष्णव पुत्रकी प्राप्तिका अत्यन्त एकाग्रतापूर्वक) भगवान्‌ शिवकी प्रसन्नताके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 115.659)
- **Original**: बर माँगा। गन्धर्वकी बात सुनकर दीनोंके स्वामी लिये तप करने लगे। उस समय उनके मनमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 115.660)
- **Original**: दीनबन्धु सनातन भगवान्‌ चन्द्रशेखर हँसे और बड़ी दीनता थी, वे दयनीय हो रहे थे।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 115.661)
- **Original**: उस दीन सेबकसे बोले। कृपानिधान वसिष्ठ मुनिने गन्धर्वराजकों शिवके कबच, स्तोत्र तथा द्वादशाक्षर-मन्त्रका उपदेश दिया। दीर्घकालतक निराहार रहकर उपासना एबं जप-तप करनेपर भगवान्‌ शिवने उन्हें प्रत्यक्ष दर्शन दिये। नित्य तेजःस्वरूप सनातन भगवान्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 115.662)
- **Original**: 2; शिव ब्रह्मतेजसे जाज्वल्यमान हो दसों दिशाओंको
- **Translation**: 

---

### Verse 10 (Vaivtpuran 115.663)
- **Original**: प्रकाशित कर रहे थे। उनके प्रसन्न मुखपर मन्द
- **Translation**: 

---

### Verse 11 (Vaivtpuran 115.664)
- **Original**: ” हास्यकी छठा छा रही थी। भक्तोंपर अनुग्रह करनेवाले वे भगवान्‌ तपोरूप हैं, तपस्याके बीज
- **Translation**: 

---

### Verse 12 (Vaivtpuran 115.665)
- **Original**: हैं, तपका फल देनेवाले हैं और स्वयं ही - 30 तपस्याके फल हैं। शरणमें आये हुए भक्तको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 115.666)
- **Original**: . श्रीमहादेवजीने कहा--गन्धर्वराज! तुमने वे समस्त सम्पत्तियाँ प्रदान करते हैं। उस समय । जो एक बर (हरिभक्ति)-को माँगा है, उसीसे ले दिगम्बर-वेषमें वृषभपर आरूढ थे, उन्होंने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 115.667)
- **Original**: तुम कृतार्थ होओगे। दूसरा बर तो चबाये हुएको हाथोंमें त्रिशुल और पट्टिश ले रखे थे। उनकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 115.668)
- **Original**: चबानामात्र है। वत्स! जिसकी श्रीहरिमें सुदृढ़ अज्जकान्ति शुद्ध स्फटिकके समान निर्मल थी।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 115.669)
- **Original**: एवं सर्वमड्रलमयों भक्ति है, वह खेल-खेलमें उनके तीन नेत्र थे और उन्होंने मस्तकपर चन्द्रमाका
- **Translation**: 

---

### Verse 17 (Vaivtpuran 115.670)
- **Original**: ही सब कुछ करनेमें समर्थ है। भगवद्धक्त पुरुष मुकुट धारण कर रखा था। उनका जटाजूट तपाये
- **Translation**: 

---

### Verse 18 (Vaivtpuran 115.671)
- **Original**: अपने कुलकी और नानाके कुलकी असंख्य हुए सुवर्णकी प्रभाको छीने लेता था। कण्ठमें नील
- **Translation**: 

---

### Verse 19 (Vaivtpuran 115.672)
- **Original**: पीढ़ियोंका उद्धार करके निश्चय हो गोलोकमें चिह् और कंधेपर नागका यज्ञोपवीत शोभा दे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 115.673)
- **Original**: जाता है। करोड़ों जन्मोंमें उपार्जित त्रिबिध
- **Translation**: 

---

