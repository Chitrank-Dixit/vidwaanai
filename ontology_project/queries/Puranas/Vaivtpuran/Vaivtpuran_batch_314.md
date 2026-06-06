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

### Verse 1 (Vaivtpuran 15.6633)
- **Original**: अपने स्तनके दूध तथा उपहारसे मेरा पालन- जन्म होता है, बे उन्हीं योनियोंमें निरन्तर रहते हुए
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6634)
- **Original**: पोषण किया है। अत; मैं उनका पोष्य पुत्र हूँ और निर्वुति लाभ करते हैं। वे चाहे संत हों अथवा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6635)
- **Original**: पोषण करनेके कारण ये मेरी माताएँ हैं। साथ ही मूर्ख हों, जिन्हें कर्मभोगके परिणामस्वरूप जिस
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6636)
- **Original**: मैं उन प्रकृतिदेवी (पार्वती)-का भी पुत्र हूँ; योनिकी प्राप्ति हुई है, वे विष्णुमायासे मोहित
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6637)
- **Original**: क्योंकि तुम्हारे स्वामी शंकरजीके वीर्यसे उत्पन्न होकर उसी योनिको बहुत बढ़कर समझते हैं। जो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6638)
- **Original**: हुआ हूँ। नन्दिकेश्वर! मैं गिरिराजनन्दिनीके गर्भसे सनातनी विष्णुमाया सबकी आदि, सर्वस्व प्रदान
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6639)
- **Original**: उत्पन्न नहीं हुआ हूँ, अतः जैसे वे मेरी धर्ममाता करनेवाली और विश्वका मज्जल करनेवाली हैं,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.6640)
- **Original**: हैं, वैसे ही. ये कृत्तिकाएँ भी सर्वसम्मतिसे मेरी उन्हीं जगज्जननीने इस समय भारतवर्षमें शैलराजकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.6641)
- **Original**: धर्म-माताएँ हैं; क्योंकि स्तन पिलानेवाली (धाय), पत्नीके गर्भसे जन्म धारण किया है और दारुण
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.6642)
- **Original**: गर्भमें धारण करनेवाली (जननी), भोजन देनेवाली तपस्या करके शंकरको पतिरूपमें प्राप्त किया है।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.6643)
- **Original**: (पाचिका), गुरुपत्री, अभीष्ट देवताकौ पत्नी, ब्रह्मासे लेकर तृणपर्यन्त सारी सृष्टि कृत्रिम है, [पिताकी पत्नी (सौतेली माता), कन्या, बहिन, अतएव मिथ्या ही है। सभी श्रीकृष्णसे उत्पन्न हुए
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.6644)
- **Original**: पुत्रवधू, पन्नीकी माता (सास), माताकी माता हैं और समय आनेपर केवल श्रीकृष्णमें ही
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.6645)
- **Original**: (नानी), पिताकी माता (दादी), सहोदर भाईकी विलीन हो जाते हैं। प्रत्येक कल्पमें सृष्टिके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.6646)
- **Original**: पत्री, माताकौ बहिन (मौसी), पिताकी बहिन विधानमें मैं नित्य होते हुए भी मायासे आबद्ध
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.6647)
- **Original**: (बूआ) तथा मामी-ये सोलह मनुष्योंकी वेदविहित होकर जन्म-धारण करता हूँ, उस समय प्रत्येक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.6648)
- **Original**: माताएँ कहलाती हैं।* ये कृत्तिकाएँ सम्पूर्ण जन्ममें जगज्जननी पार्वती मेरी माता होती हैं।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.6649)
- **Original**: सिद्धियोंकी ज्ञाता, परमैश्वर्यसम्प्न और तीनों जगतूमें जितनी नारियाँ हैं, वे सभी प्रकृतिसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.6650)
- **Original**: लोकोंमें पूजित हैं। ये थ्षुद्र नहीं हैं, बल्कि उत्पन्न हुई हैं। उनमेंसे कुछ प्रकृतिकी अंशभूता
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6651)
- **Original**: ब्रह्माकी कन्याएँ हैं। तुम भी सत्त्वसम्पन्न तथा हैं तो कुछ कलात्मिका तथा कुछ कलांशके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6652)
- **Original**: शम्भुके पुत्रके समान हो और विष्णुने तुम्हें भेजा अंशसे प्रकट हुई हैं। ये ज्ञानसम्पन्ना योगिनी
- **Translation**: 

---

