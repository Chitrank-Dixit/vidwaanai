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

### Verse 1 (Vaivtpuran 13.10522)
- **Original**: परिपूर्ण है; आप अपने उसी रूपका हमें दर्शन उन्हें प्रणाम किया। शिवजी उन्हें उत्तम आशीर्वाद
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10523)
- **Original**: कराइये। जिसकी दो भुजाएँ हैं; कमनीय किशोर दे शीघ्र ही उनसे वार्तालापके लिये उद्यत हुए।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10524)
- **Original**: अवस्था है; श्यामसुन्दर रूप है; हाथमें विनोदकी उस समय उनके प्रसन्नमुखपर मुस्कराहट खेल
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10525)
- **Original**: साधनभूता मुरली है; जो पीताम्बरधारी है; जिसके रही थी और वे उन भक्तजनोंपर अनुग्रह करनेके एक मुख और दो नेत्र हैं, वे चन्दन और अगुरुसे लिये कातर हो चुके थे। चर्चित हैं; जिसके प्रसन्नमुखपर मन्द मुस्कानकी भगवान्‌ शिवने पूछा--पार्वतीके सरोवरमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10526)
- **Original**: प्रभा फैल रही है; जो रत्लमय अलंकारोंसे प्रवेश करके कमल लेनेवाले तुमलोग कौन हो?
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10527)
- **Original**: विभूषित है। जिसका वक्ष;स्थल मणिराज कौस्तुभकी पार्वतीके ब्रतकी पूर्तिक लिये एक लाख यक्ष
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10528)
- **Original**: कान्तिसे अत्यन्त उज्ज्वल दिखायी देता है; उस सरोवरकी रक्षा करते हैं। पार्वती पतिविषयक जिसकी चूड़ामें मोरका पंख लगा है; जो सौभाग्यकी वृद्धिके लिये जब त्रैमासिक व्रत
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10529)
- **Original**: मालतीकी मालासे विभूष्ति है; पारिजातके आरम्भ करती हैं, तब वे लगातार तीन महीनेतक
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10530)
- **Original**: फूलोंके हारोंसे अलंकृत है; करोड़ों कन्दर्पोंके श्रीहरिको भक्तिभावसे प्रतिदिन एक सहस्न कमल
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10531)
- **Original**: लावण्यका मनोहर लीलाधाम है; समूह-की- चढ़ाती हैं।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10532)
- **Original**: समूह गोपियाँ मन्‍्द मुस्कान और बाँकी चितबनसे भगवान्‌ शिवका यह बचन सुनकर वे तीनों
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10533)
- **Original**: जिसकी ओर देखा करती हैं; जो नूतन यौबनसे वैष्णब भयभीत हो भक्तिसे मस्तक झुका हाथ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10534)
- **Original**: सम्पन्न तथा राधाके वक्षःस्थलपर विराजमान है; जोड़कर बोले। ब्रह्मा आदि जिसकी स्तुति करते हैं; जो सबके गन्धरवोने कहा--प्रभो! हमलोग गन्धर्वराज
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10535)
- **Original**: लिये वन्दनीय, चिन्तनीय और वाञ्छनीय है और गन्धवाहके पुत्र गन्धवॉमें श्रेष्ठ हैं। महेश्वर! हम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10536)
- **Original**: जो स्वात्माराम, पूर्णकाम तथा भक्तोंपर अनुग्रहके लोग प्रतिदिन श्रीहरिकों कमल चढ़ाकर ही जल
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10537)
- **Original**: लिये कातर रहनेवाला है;--आपके उसी रूपका पीते हैं। हे नाथ! हम यह नहीं जानते थे कि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10538)
- **Original**: हम दर्शन करना चाहते हैं। ऐसा कहकर वे पार्वतीके द्वारा इस सरोवरकी रक्षा की जाती है। श्रेष्ठ गन्धर्व भगवान्‌ शंकरके सामने खड़े हो गये। आप यह सारे कमल ले लीजिये और अपने श्रीकृष्णके रूपका बर्णन सुनकर भगवान्‌ ब्रतकों सफल बनाइये। महादेव! हम आज कमल
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10539)
- **Original**: शंकरके श्रीअज्जोंमें रोमाझ् हों आया। उनके नेत्रोंमें नहीं चढ़ायेंगे और जल भी नहीं पीयेंगे। हमने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10540)
- **Original**: आँसू भर आये। वे गन्धर्वोकी उक्त बातें सुनकर आपको ही वे कमल अर्पित कर दिये। जिनके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10541)
- **Original**: उनसे इस प्रकार बोले--' मैंने यह जान लिया था चरण-कमलका प्रतिदिन चिन्तन करके हम
- **Translation**: 

---

