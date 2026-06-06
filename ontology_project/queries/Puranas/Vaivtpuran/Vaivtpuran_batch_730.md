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

### Verse 1 (Vaivtpuran 543.12914)
- **Original**: + श्रीकृष्णजन्मखण्ड + 565 ।([(77[8](70(77]]]7007 0] ] 3] 3] 887 28855] दक्षके प्रति बड़ा रोष था। सतीके मनमें पिता
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12915)
- **Original**: धारण करना असम्भव है।' यह आकाशवाणी आदिके प्रति मोह था; इसलिये उन्होंने यत्रपूर्वक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12916)
- **Original**: सुनकर यौवनके गव॑से भरी हुई पार्वती हँसकर पतिदेवको उस यज्ञमें चलनेके लिये समझाया।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12917)
- **Original**: चुप हो रहीं। वह मन-ही-मन सोचने लगीं कि जब किसी तरह उन्हें वहाँ ले जानेमें वे समर्थ
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12918)
- **Original**: “जो मेरे दूसरे जन्मकी अस्थि और भस्मको धारण न हो सकीं, तब स्वयं चछल हो उठीं और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12919)
- **Original**: करते हैं; वे इस जन्ममें मुझे सयानी हुई देख पतिकी आज्ञा प्राप्त किये बिना ही दर्पवश पिताके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12920)
- **Original**: कैसे नहीं ग्रहण करेंगे। जो चतुर होकर भी मेरे घर चली आयीं। पतिके शापसे वहाँ उनका दर्प-
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12921)
- **Original**: शोकसे समूचे ब्रह्माण्डमें भटकते फिरे; वे ही भजन हुआ। पिताने उनसे बाततक नहीं कौ।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12922)
- **Original**: मुझ परम सुन्दरीको अपनी आँखोंसे देख लेनेपर वाणीमात्रसे भी पुत्रीका सत्कार नहीं किया। इतना
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12923)
- **Original**: क्‍यों नहीं ग्रहण करेंगे ? जिन कृपानिधानने मेरे ही नहीं, उन्हें वहाँ पतिकी निन्‍्दा भी सुननी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12924)
- **Original**: लिये दक्षयज्ञका विध्वंस कर डाला था; वे अपनी पड़ी। उसे सुनकर स्वाभिमानवश सतीने अपने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12925)
- **Original**: जन्म-जन्मकी पत्नी मुझ पार्वतीको क्‍यों नहीं ग्रहण शरीरको त्याग दिया। करेंगे? पूर्वजन्मसे ही जो जिसकी पत्नो है और प्रिये! इस प्रकार सतीके दर्प-भड्डका वृत्तान्त जिसका जो पति है, उन दोनोंमें यहाँ भेद कैसे कहा गया। अब तुम उनके जन्मान्तर तथा दर्प-
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12926)
- **Original**: हो सकता है? क्योंकि प्रारब्धको कोई पलट नहीं दलनकी कथा सुनो। सतीने शीघ्र ही गिरिराज
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12927)
- **Original**: सकता।' हिमालयकी पत्नी मेनाके गर्भसे जन्म ग्रहण
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12928)
- **Original**: । अत्यन्त अभिमानके कारण अपनेको समस्त किया। शिवने प्रेमवश सतीकी चिताका भस्म और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12929)
- **Original**: रूप और गुणोंका आधार मानकर साध्वी शिवाने उनकी अस्थियाँ ग्रहण कीं। अस्थियोंकी तो माला
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12930)
- **Original**: तप नहीं किया। उन्होंने शिवको ईश्वर नहीं बनायी और भस्मसे अड्भरागका काम लिया। वे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12931)
- **Original**: समझा। “समस्त सुन्दरियोंमें मुझसे बढ़कर सुन्दरी प्रेमवश बार-बार सतीको याद करते और उनके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12932)
- **Original**: दूसरी कोई नहीं है '-यह धारणा हृदयमें लेकर विरहमें इधर-उधर घूमते रहते थे। उधर मेनाने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12933)
- **Original**: शिवादेवी गर्ववश तपस्यामें नहीं प्रवृत्त हुईं। वे देवीको जन्म दिया। उनकी आकृति बड़ी ही
- **Translation**: 

---

