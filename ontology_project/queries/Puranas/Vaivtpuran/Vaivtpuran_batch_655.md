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

### Verse 1 (Vaivtpuran 67.5895)
- **Original**: मनोहर उपहारोंसे सजी हुई हों, दान करनी जन्मपर्यन्त स्वामीके धनकी वृद्धिके निमित्त यत्रपूर्वक्ष चाहिये। एक हजार तीन सौ साठ ब्राह्मणोंको श्रीकृष्णकों एक लाख र्रेन्द्रसार समर्पित करना
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.5896)
- **Original**: भोजन तथा एक हजार तीन सौ साठ तिलकी चाहिये। व्रतीकों चाहिये कि ब्रतकालमें सम्पत्तिको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.5897)
- **Original**: आहुतियाँ देनेका विधान है। फिर व्रत समाप्त वृद्धिके हेतु झाँल-मजीरा आदि नाना प्रकारके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.5898)
- **Original**: हो जानेपर विधिपूर्वक एक हजार तीन सौ साठ उत्तम बाजे बजाकर श्रीहरिको सुनावे। स्वामीकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.5899)
- **Original**: स्वर्णमुद्राओंकी दक्षिणा देनी चाहिये। इसके भोगवृद्धिके लिये भक्तिपूर्वक श्रीहरिको मनोहर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.5900)
- **Original**: अतिरिक्त ब्रत-समाप्तिके दिन दूसरी दक्षिणा भी खीर और शक्करयुक्त घो तथा पूड़ीका भोग प्रदान
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.5901)
- **Original**: बतलाऊँगा। देवि! इस व्रतका फल यही है कि करे। हरिभक्तिकी विशेष उन्नतिके लिये स्वेच्छानुसार
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.5902)
- **Original**: श्रीहरिमें भक्ति दृढ़ हो जाती है। श्रीहरिके सदृश सुगन्धित पुष्पोंकी एक लाख माला, जो टूटी हुई
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.5903)
- **Original**: तोनों भुवनोंमें विख्यात पुत्र उत्पन्न होता है और न हों, भक्तिपूर्वक श्रीहरिको अर्पित करनी चाहिये।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.5904)
- **Original**: सौन्दर्य, पतिसौभाग्य, ऐश्वर्य और अतुल धनकी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.5905)
- **Original**: + गणपतिखण्ड « 299 4.4 4 4 2 3 2 8 8 2 2 2 9 2 2
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.5906)
- **Original**: 8 2 2 2 ) 02000 ]05( 2 ] 0240 4448(43].] प्राप्ति होती है। महेश्वरि! यह ब्रत प्रत्येक जन्ममें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.5907)
- **Original**: भी इस ब्रतका अनुष्ठान करो। साध्थि! तुम्हें पुत्र समस्त वाज्छित सिद्धियोंका बीज है, जिसका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.5908)
- **Original**: उत्पन्न होगा। यों कहकर शिवजी चुप हो गये। मैंने इस प्रकार वर्णन किया है; अत: देवि! तुम (अध्याय 4) डर 32 अं: 0.00 पुण्यक-ब्रतकी माहात्म्य-कथाका कथन श्रीनारायण कहते हैं--नारद! इस प्रकार
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.5909)
- **Original**: ग्रहण कीजिये; क्योंकि तात! हम दोनों पुत्रहीनोंको ब्रतके विधानकों सुनकर दुर्गाका मन प्रसन्नतासे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.5910)
- **Original**: पुत्रके बिना इन सबसे क्‍या प्रयोजन है? साक्षात्‌ खिल उठा। तत्पश्चात्‌ उन्होंने अपने स्वामी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.5911)
- **Original**: ब्रह्माजीसे यों कहकर शतरूपा फूट-फूटकर रुदन शिवजीसे दिव्य एवं शुभकारिणी ब्रत-कथाके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.5912)
- **Original**: करने लगी। तब उसकी ओर देखकर कृपालु विषयमें जिज्ञासा प्रकट की। ब्रह्माजीने कहा। श्रीपार्वतीजीने पूछा--नाथ ! यह व्रत तथा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.5913)
- **Original**: . ब्रह्माजी बोले--वत्से ! जो समस्त ऐश्वर्य इसका फल और विधान बड़ा ही अद्भुत है।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.5914)
- **Original**: आदिका कारणरूप, सम्पूर्ण मनोरथोंका दाता तथा भला, किसने इस ब्रतको प्रकाशित किया है ?
- **Translation**: 

---

