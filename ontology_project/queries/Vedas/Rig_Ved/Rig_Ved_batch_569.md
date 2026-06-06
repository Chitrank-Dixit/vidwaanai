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

### Verse 1 (Rig Ved 0.11361)
- **Original**: हे पूषन्‌ देव ! आप हमारे यज्ञादि कार्य को सफलता के लिए गौ, अश्व॒ सेवक एवं अन्न प्रदान करें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11362)
- **Original**: [ सूक्त - 54 ] [ऋषि - भरद्वाज बा्हस्पत्य । देवता -पूषा । छन्द - गायत्री ] 4945, सं पूषन्‌ यिदुषा नय यो अज्जसानुशासति। य एवेदमिति ब्रवतू
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11363)
- **Original**: हे पूषन्‌देव ! आप हमें ऐसे श्रेष्ठ मार्गदर्शक के पास पहुँचाएँ, जो हमें उत्तम मार्ग एवं धन प्राप्त करने का मार्ग बताएँ
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11364)
- **Original**: 4946. समु पृष्णा गमेमहि यो गृहाँ अभिशासति
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11365)
- **Original**: इम एवेति च ब्रवत्‌
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11366)
- **Original**: हे पूषन्‌देव ! आप हमें ऐसे पुरुष से मिलाएँ, जो घर को अनुशासित रखने का मार्गदर्शन दे
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11367)
- **Original**: 4947. पृष्णक्षक्रं न रिष्यति न कोशो5व पद्मयते
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11368)
- **Original**: नो अस्य व्यथते पवि:
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11369)
- **Original**: पूषनूदेव का चक्र कभी भी दूषित नहीं होता है । इसकी धार सदैव तीक्ष्ण रहती है
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11370)
- **Original**: मं0 6 सृ0 54 79 4948. यो अस्मै हविषाविधन्न तं पूषापि मृष्यते । प्रथमो विन्दते वसु
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11371)
- **Original**: जो याजक ऐसे पूषन्‌देव के लिए आहुति प्रदान करता है । उसे कोई कष्ट नहीं होता है एवं उसे पूषादेव कृपा करके प्रथप्त (श्रेष्ठ) धन प्रदान करते हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11372)
- **Original**: 4949. पूषा गा अन्वेतु नः पूषा रक्षत्वर्वत:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11373)
- **Original**: पूषा वाज॑ सनोतु नः
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11374)
- **Original**: पूषनूदेव हमारी गौओं की, घोड़ों की रक्षा करें एवं हमें अत्र एवं धन प्रदान करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11375)
- **Original**: 4950. पूषन्ननु प्र गा इहि यजमानस्य सुन्व॒तः । अस्माक स्तुवतामुत
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11376)
- **Original**: हे पूषनूदेव ! यज्ञ कर्म करने वालों को तथा हम स्तोताओं को अनुकूल गौएँ प्राप्त हों
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11377)
- **Original**: 4951. माकिनेंशन्माकीं रिषन्माकीं सं शारि केवटे। अथारिष्टाभिरा गहि
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11378)
- **Original**: हे पूषन्‌देव ! आप हमारी गौओं को नष्ट न करें, कुएँ में गिरकर या अन्य प्रकार से नष्ट न होने दें । आपसे सुरक्षित गौएँ सायंकाल हमारे पास लौट आएँ
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11379)
- **Original**: 4952. शृण्वन्तं पृषणं बयमिर्यमनष्टवेदसम्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11380)
- **Original**: ईशान राय ईमहे
- **Translation**: 

---

