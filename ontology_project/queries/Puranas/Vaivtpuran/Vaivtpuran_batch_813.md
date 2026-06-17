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

### Verse 1 (Vaivtpuran 543.14574)
- **Original**: उस शापके कारण कुछ दिनोंतक मुझसे तुम्हारा समस्त गोकुलवासियोंकी शोभा तुम्हारे साथ रहनेसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14575)
- **Original**: वियोग रहेगा। शापकी अवधि समाप्त होनेपर फिर हो है। रासेश्वर! जैसे स्वर्गमें देवराज इन्द्रसे ही
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14576)
- **Original**: हम दोनोंका मिलन होगा। फिर मैं गोलोकवासी अमरावतीपुरी शोभित होती है, उसी प्रकार
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14577)
- **Original**: गोपों और गोपाड्नाओंके साथ अपने परमधाम रासमण्डलको भी तुमसे ही मनोहर शोभा प्रास्त
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14578)
- **Original**: गोलोकको चलूँगा। इस समय मैं तुमसे कुछ होती है। जैसे बलवान्‌ सिंह अन्यान्य बनोंकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14579)
- **Original**: आध्यात्मिक ज्ञानकी बातें कहता हूँ, सुनो। यह शोभा, स्वामी और सहारा है, उसी प्रकार तुम्हीं
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14580)
- **Original**: सारभूत ज्ञान शोकका नाशक, आनन्दवर्धक तथा वृन्दावनके वृक्षोंकी शोभा, संरक्षक और आश्रयदाता
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14581)
- **Original**: मनकों सुख देनेवाला है। मैं सबका अन्‍्तरात्मा हो। जैसे गाय अपने बछड़ेको न पाकर व्याकुल
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14582)
- **Original**: और समस्त कर्मोंसे निर्लिस हूँ। सबमें सर्वत्र हो डकराने लगती है, उसी प्रकार माता यशोदा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14583)
- **Original**: विद्यमान रहकर भी कभी किसीके दृष्टिपथमें नहीं तुम्हारे बिना शोकसागरमें निमग्र हो जाती हैं। जैसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14584)
- **Original**: आता हूँ। जैसे वायु सर्वत्र सभी बस्तुओंमें तपे हुए पात्रमें धान्ययाशि जल जाती है, उसी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14585)
- **Original**: विचरती है, किंतु किसीसे लिप्त नहीं होती; उसी प्रकार तुम्हारे बिना नन्दजीका हृदय दग्ध होने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14586)
- **Original**: प्रकार मैं समस्त कर्मोंका साक्षी हूँ। उन कमोंसे लगता है और प्राण आन्दोलित हो उठते हैं।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14587)
- **Original**: लिप्त नहीं होता हूँ। सर्वत्र समस्त जीवधारियोंमें यों कहकर अत्यन्त प्रेमके कारण राधा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14588)
- **Original**: जो जीवात्मा हैं, बे सब मेरे ही प्रतिबिम्ब हैं। श्रीहरिके चरणोंमें गिर पड़ीं। श्रीहरिने पुनः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14589)
- **Original**: जीवात्मा सदा समस्त कर्मोंका कर्ता और उनके अध्यात्म-ज्ञानकी बातें कहकर उन्हें समझाया-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14590)
- **Original**: शुभाशुभ फलोंका भोक्ता है। जैसे जलके घड़ोंमें बुझाया। नारद! आध्यात्मिक महायोग उसी तरह चन्द्रमा और सूर्यके मण्डलका पृथक्‌-पृथक्‌ मोहके उच्छेदका कारण कहा गया है, जैसे तोखी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14591)
- **Original**: प्रतिबिम्ब दिखायी देता है, किंतु उन घड़ोंके फूट धारवाला कुठार वृक्षोंके काटनेमें हेतु होता है।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14592)
- **Original**: जानेपर वे सारे प्रतिबिम्ब चन्द्रमा और सूर्यमें ही नारदने कहा--वेदवेत्ताओंमें श्रेष्ठ भगवन्‌!
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14593)
- **Original**: बिलीन हो जाते हैं; उसी प्रकार अन्त:करणरूपी लाकोंके शोकका उच्छेद करनेवाले आध्यात्मिक
- **Translation**: 

---

