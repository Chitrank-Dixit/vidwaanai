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

### Verse 1 (Bramha 0.6281)
- **Original**: है। वही सत्‌, असत्‌ और ज्ञानात्मा है। आपके उस है, जो सर्वत्र व्यापक हैं, जो कारणरूपसे एक,
- **Translation**: 

---

### Verse 2 (Bramha 0.6282)
- **Original**: स्वरूपको मेरा प्रणाम है। भगवन्‌ ! वासुदेवरूपमें किंतु कार्यरूपसे अनेक हैं, उन परमात्माको
- **Translation**: 

---

### Verse 3 (Bramha 0.6283)
- **Original**: आपको नमस्कार है। संकर्षण-संज्ञा धारण करनेवाले बारंबार नमस्कार है। अचिन्त्य परमेश्वर ! आप
- **Translation**: 

---

### Verse 4 (Bramha 0.6284)
- **Original**: आपको नमस्कार है। प्रद्यम्न कहलानेवाले आपको शब्द (वैदिक मन्त्र)-रूप और हविःस्वरूप हैं।
- **Translation**: 

---

### Verse 5 (Bramha 0.6285)
- **Original**: नमस्कार है और अनिरुद्ध नामसे पुकारे जानेवाले आपको नमस्कार है। प्रभो! आप प्रकृतिसे परे
- **Translation**: 

---

### Verse 6 (Bramha 0.6286)
- **Original**: आपको नमस्कार है।' विज्ञानस्वरूप हैं। आपको नमस्कार है। आप ही
- **Translation**: 

---

### Verse 7 (Bramha 0.6287)
- **Original**: इस प्रकार जलके भीतर यदुवंशी अक्रूरने भूतात्मा, इन्द्रियात्मा, प्रधानात्मा, जीवात्मा और , सर्वेश्वर श्रीकृष्णकी स्तुति करके मानसिक धूप परमात्मा हैं। इस प्रकार एक होते हुए भी आप
- **Translation**: 

---

### Verse 8 (Bramha 0.6288)
- **Original**: और पुष्पोंद्रारा उनका पूजन किया। अन्य विषयोंका पाँच प्रकारसे स्थित हैं। सर्वधर्मात्मन्‌ महेश्वर!
- **Translation**: 

---

### Verse 9 (Bramha 0.6289)
- **Original**: चिन्तन छोड़कर मनको उन ब्रह्मभूत परमात्मामें आप ही क्षर और अक्षर हैं। मुझपर प्रसन्न होइये।
- **Translation**: 

---

### Verse 10 (Bramha 0.6290)
- **Original**: लगा दीर्घकालतक ध्यान किया। तत्पश्चात्‌ समाधिसे ब्रह्मा, विष्णु तथा शिव आदि नामोंसे आपका ही
- **Translation**: 

---

### Verse 11 (Bramha 0.6291)
- **Original**: विरत हो अपनेको कृतार्थ मानते हुए यमुना- वर्णन किया जाता है। भगवन्‌ ! आपके स्वरूप,
- **Translation**: 

---

### Verse 12 (Bramha 0.6292)
- **Original**: जलसे निकलकर वे पुनः रथके समीप आये। प्रयोजत और नाम आदि सभी अनिर्वचनीय हैं।
- **Translation**: 

---

### Verse 13 (Bramha 0.6293)
- **Original**: आनेपर उन्होंने बलराम और श्रोकृष्णको पूर्ववत्‌ आप परमेश्वरकों मेरा नमस्कार है। नाथ ! जहाँ
- **Translation**: 

---

### Verse 14 (Bramha 0.6294)
- **Original**: बैठे देखा। अक्रूरजीके नेत्रोंसे निस्मथका आभास नाम और जाति आदि कल्पनाओंका अस्तित्व नहीं
- **Translation**: 

---

### Verse 15 (Bramha 0.6295)
- **Original**: मिलता था। यह देख श्रीकृष्णने उनसे कहा-- 'है, वह नित्य, अविकारी और अजन्मा परब्रह्म आप
- **Translation**: 

---

### Verse 16 (Bramha 0.6296)
- **Original**: “अक्ूस्जी! आपने यमुनाके जलमें कौन-सी आश्चर्यकी ही हैं। कल्पनाके बिना-कोई व्यावहारिक नाम
- **Translation**: 

---

### Verse 17 (Bramha 0.6297)
- **Original**: बात देखी है, जो आपके नेत्र आश्षर्यचकित रखे बिना किसी भी पदार्थका ज्ञान नहीं होता।
- **Translation**: 

---

### Verse 18 (Bramha 0.6298)
- **Original**: दिखायी देते हैं?" इसीलिये कृष्ण, अच्युत, अनन्त और विष्णु आदि
- **Translation**: 

---

### Verse 19 (Bramha 0.6299)
- **Original**: अक़वूर बोले--अच्युत ! जलके भीतर मैंने नामोंसे आपकी स्तुति की जाती है। सर्वात्मर्‌! आप
- **Translation**: 

---

### Verse 20 (Bramha 0.6300)
- **Original**: जो आश्चर्य देखा है, उसे यहीं अपने सामने अजन्मा परमेश्वर हैं। जगत्‌में जितनी कल्पनाएँ हैं,
- **Translation**: 

---

