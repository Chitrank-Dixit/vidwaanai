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

### Verse 1 (Vaivtpuran 5.2373)
- **Original**: यदा महेन्द्र: पप्रच्छ तत्त्वज्ञानं सदाशिवम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 5.2374)
- **Original**: प्रप्रच्छ शब्दशास्त्र च महेन्द्रश वृहस्पतिम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 5.2375)
- **Original**: तदा त्वत्तो वर प्राप्प दिव्यवर्षमहखकम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 5.2376)
- **Original**: अध्यापिताक्ष ये शिष्या यैरधोत॑ मुत्रीश्ररै:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 5.2377)
- **Original**: त्य॑ संस्तुता पूजिता च॑ मुनीन्द्रैर्मनुभानवैः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 5.2378)
- **Original**: जड़ी भूत: सहस्नास्य: परश्ृवक्त्रश्॒तुर्मुख:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 5.2379)
- **Original**: इत्युक्चा. याज्ञवल्क्यश्ष॒ भक्तिनम्नात्मकन्धर:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 5.2380)
- **Original**: तदा ज्योति:स्वरूपा सा तेन दृष्टाप्युवाच तम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 5.2381)
- **Original**: याज्ञवल्क्यकृत॑ याणीस्तोत्रमेततु यः. पठेतू
- **Translation**: 

---

### Verse 10 (Vaivtpuran 5.2382)
- **Original**: महापूर्खध दुर्मेधा वर्षमेके यदा पढेतू। स पण्डितश्व॒ मेधावी सुकविश्च भवेद्‌ धुवम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 5.2383)
- **Original**: (प्रकृतिखण्ड 5। 6--36)
- **Translation**: 

---

### Verse 12 (Vaivtpuran 5.2384)
- **Original**: + प्रकृतिखण्ड * 109 %##%###4%%4%###%##### ## #######% #% %# ##%%%##%% 54 %%%%%$#%%%%#%$%%$%%%% कक श्क फफ फफ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 5.2385)
- **Original**: कक विष्णुपत्री लक्ष्मी, सरस्वती एवं गड्राका परस्पर शापवजश भारतवर्षमें पधारना भगवान्‌ नारायण कहते हैं--नारद! वे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 5.2386)
- **Original**: कि श्रीहरि मेरी अपेक्षा गड़ासे अधिक प्रेम करते भ्रगवती सरस्वती स्वयं वैकुण्ठमें भगवान्‌ श्रीहरिके हैं। तब उन्होंने श्रीहरिको कुछ कड़े शब्द कह पास रहती हैं। पारस्परिक कलहके कारण गड्जाने दिये। फिर वे गड्भापर क्रोध करके कठोर बर्ताव इन्हें शाप दे दिया था। अत: ये भारतवर्षमें अपनी करने लगीं। तब शान्तस्वरूपा, क्षमामयी लक्ष्मीने एक कलासे पधारकर नदीरूपमें प्रकट हुईं। मुने! उनको रोक दिया। इसपर सरस्वतीने लक्ष्मीको सरस्वती नदी पुण्य प्रदान करनेवाली, पुण्यरूपा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 5.2387)
- **Original**: गड्भगाका पक्ष करनेवाली मानकर आवेशमें शाप और पुण्यतीर्थ-स्वरूपिणी हैं। पुण्यात्मा पुरुषोंको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 5.2388)
- **Original**: दे दिया कि “तुम निश्चय ही वृक्षरूपा और चाहिये कि वे इनका सेवन करें। इनके तटपर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 5.2389)
- **Original**: नदीरूपा हो जाओगी।' पुण्यवानोंकी ही स्थिति है। ये तपस्वियोंके लिये लक्ष्मीने सरस्वतीके इस शापको सुन लिया; तपोरूपा हैं और तपस्थाका फल भी इनसे कोई
- **Translation**: 

---

### Verse 18 (Vaivtpuran 5.2390)
- **Original**: परंतु स्वयं बदलेमें सरस्वतीकों शाप देना तो दूर अलग वस्तु नहीं है। किये हुए सब पाप
- **Translation**: 

---

### Verse 19 (Vaivtpuran 5.2391)
- **Original**: रहा, उनके मनमें तनिक-सा क्रोध भी उत्पन्न लकड़ीके समान हैं। उन्हें जलानेके लिये ये नहीं हुआ। वे वहाँ शान्त बैठी रहों और प्रज्वलित अग्रिस्वरूपा हैं। भूमण्डलपर रहनेवाले
- **Translation**: 

---

### Verse 20 (Vaivtpuran 5.2392)
- **Original**: सरस्वतीके हाथको अपने हाथसे पकड़ लिया। जो मानव इनकी महिमा जानते हुए इनके तटपर
- **Translation**: 

---

